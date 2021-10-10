  var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
    function fn(name) {
    var  x =document.getElementById("frm1" )
   console.log(name);
   var a = '/validate/';
console.log(a,name);

      $.ajax({
     url: '/validate/',
       data: {
          'name': name
        },
        dataType: 'json',
        success: function(data) {
        console.log("Operation sucessful");
         if (data.is_taken) {
            console.log(data.error_message);
            console.log(data.name);
            console.log(data.name2);
              console.log(data.detail);
            console.log(data.price);

            document.getElementById("product-id").innerHTML = 'ID'+data.id;
            document.getElementById("product-name").innerHTML = 'Name : '+data.name;

            document.getElementById("product-detail").innerHTML ='Detail : '+ data.detail;
            document.getElementById("product-price").innerHTML = 'Price : '+data.price+ ' $';
            document.getElementById("product-image").src = data.image;
            var b= data.size;
            console.log(Object.values(b));
                        document.getElementById("product-size").innerHTML = 'Size : ' + b;




          }
        }
      });

  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function cart(name) {
    var  x =document.getElementById("frm1" )
   console.log(name);
   window.confirm(name + "Added to Cart")
       console.log("ajax is running...")
      $.ajax({

     url: '/cart_add/',
       data: {
          'name': name
        },
        dataType: 'json',
        success: function(data) {
        console.log("Operation sucessful");
         if (data.is_taken) {
            console.log(data.error_message);
            console.log(data.name);
            console.log(data.name2);
              console.log(data.detail);
            console.log(data.price);
            document.getElementById("product-id").innerHTML = data.id;
            document.getElementById("product-name").innerHTML = data.name;
            document.getElementById("product-detail").innerHTML = data.detail;
            document.getElementById("product-price").innerHTML = data.price;
            document.getElementById("product-image").src = data.image;
            window.alert( data.name +" Sucessfuly Added to Cart.");
          }
        }
      });


}


function incriment(name) {
    var  x =document.getElementById("frm1" )
   console.log(name);
   window.confirm(name + "Added to Cart")

      $.ajax({

     url: '/item_increment/',
       data: {
          'name': name
        },
        dataType: 'json',
        success: function(data) {
        console.log("Operation sucessful");
         if (data.is_taken) {
            console.log(data.error_message);
            console.log(data.name);
            console.log(data.name2);
              console.log(data.detail);
            console.log(data.price);
            console.log(data.cart)
            document.getElementById("product-id").innerHTML = data.id;
            document.getElementById("product-name").innerHTML = data.name;
            document.getElementById("product-detail").innerHTML = data.detail;
            document.getElementById("product-price").innerHTML = data.price;
            document.getElementById("product-image").src = data.image;
            window.alert( data.name +" Sucessfuly Added to Cart.");
          }
        }
      });
fetch()

}