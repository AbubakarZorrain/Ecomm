from decimal import Decimal
from django.conf import settings
from django.shortcuts import redirect

from .models import Product

class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """


        id = product.id
        newItem = True
        if str(product.id) not in self.cart.keys():
            size_names = list(product.size.values_list("name", flat=True))
            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.name,
                 'quantity': 1,
                'price': str(product.price),
                'image': product.product_image.url,
                'size': list(product.size.values_list("name", flat=True)),
                'size1':product.size2,
                'size2':next(iter(size_names), None),


            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:
                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                    'image': product.product_image.url,
                    'size': list(product.size.values_list("name", flat=True)),
                'size1': product.size2

                }

        self.save()

    def save(self):
                # update the session cart
                self.session[settings.CART_SESSION_ID] = self.cart
                # mark the session as "modified" to make sure it is saved
                self.session.modified = True

    def remove(self, product):
                    """
                    Remove a product from the cart.
                    """
                    product_id = str(product.id)
                    if product_id in self.cart:
                        del self.cart[product_id]
                        self.save()
    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('medical_store_app/cart.html')
                self.save()
                break
            else:
                print("Something Wrong")





    def smalls(self, product,size):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['size1'] = size
                newItem = False
                self.save()
                break
            else:
                print("Something Wrong")
    def medium(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['size'] = 'medium'
                newItem = False
                self.save()
                break
            else:
                print("Something Wrong")

    def large(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):

                value['size'] = 'large'
                newItem = False
                self.save()
                break
            else:
                print("Something Wrong")


    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

