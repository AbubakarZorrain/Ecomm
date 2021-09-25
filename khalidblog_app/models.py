from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.db import models
from django.utils.crypto import get_random_string
import random
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Post(models.Model):
    id = models.IntegerField(unique=True, auto_created=True, primary_key=True)

    title= models.CharField(max_length=300, unique=True)
    url= models.SlugField(max_length=300)
    content= models.TextField(max_length=1500)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return 'Author : '+str(self.author)+'TiTle' + str(self.title) + 'Dated :' + str(self.pub_date)

class rand(models.Model):
    name = models.CharField(max_length=300, unique=True)
    idrandstring = get_random_string(length=32,allowed_chars='ACTG')
    unique_id = '%32x' % random.getrandbits(16 * 8)


# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True,null=True)
    def __str__(self):
        return self.name
class Procategory(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True,null=True)


    slug = models.SlugField(max_length=200,
                        db_index=True,
                        unique=True,null=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
       return self.name
class Product(models.Model):
    id = models.IntegerField(unique=True, auto_created=True, primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    price = models.CharField(max_length=100, null=True)
    size = models.ManyToManyField(Size)
    size2 = models.CharField(max_length=50,null=True)
    detail = models.CharField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    category = models.ForeignKey(Procategory,on_delete=models.CASCADE, related_name='products',null=True)
    class Meta:
        ordering = ('-date_created',)
    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=250,null=True)
    postal_code = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=100,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='items')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user',null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,
                                related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=100,null=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class Emailsubription(models.Model):

    email = models.EmailField(null=True)

class one(models.Model):
    nameone= models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.nameone

class two(models.Model):
    name = models.CharField(max_length=50,null=True)
    two = models.ManyToManyField(one)
    def __str__(self):
        return self.name

class eventimage(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='Event_images/', null=True, blank=True)


class eventvideo(models.Model):
    name = models.CharField(max_length=100, null=True)
    video = models.FileField(upload_to='Event_videos/', null=True, blank=True)

class events(models.Model):
    name = models.CharField(max_length=100, null=True)
    detail = models.CharField(max_length=1000, null=True)
    image = models.ManyToManyField(eventimage)
    video = models.ManyToManyField(eventvideo)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name