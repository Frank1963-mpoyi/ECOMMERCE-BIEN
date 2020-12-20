from django.db import models




class Customer(models.Model):
    name            = models.CharField(max_length=200, null=True)
    phone           = models.CharField(max_length=200, null=True)
    email           = models.CharField(max_length=200, null=True)
    date_created    = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name            = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    
    name            = models.CharField(max_length=200, null=True)
    price           = models.FloatField(null=True)
    category        = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description     = models.CharField(max_length=200, null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=True, null=True)
    tags            = models.ManyToManyField(Tag)
    
    
    def __str__(self):
        return self.name



#one Customer with 3 differents orders, customers can have as many order they want
# and one order can have only one customer   
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delevery', 'Out for delevery'),
        ('Delivered', 'Delivered'),
    )
    customer        = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)  
    product         = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)  
    date_created    = models.DateTimeField(auto_now_add=True, null=True)
    status          = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.product.name







'''

>>> from ecommerce.apps.system.accounts.models import *
>>> customers = Customer.objects.all()
>>> customers
<QuerySet [<Customer: Frank Mpoyi>, <Customer: Ruth Mitongu>]>
>>> customers.first()
<Customer: Frank Mpoyi>
>>> customers.last()
<Customer: Ruth Mitongu>
>>> customer1 = Customer.objects.get(name="Frank Mpoyi")
>>> customer1
<Customer: Frank Mpoyi>
>>> customer1.email # here access the attribute or(field)of Customer
'frankmpoyi63@gmail.com'

#set variable [orders = customer1.order_set.all() ]# this order in small letter is the Order class

>>> orders = customer1.order_set.all()
>>> orders
<QuerySet [<Order: Order object (1)>, <Order: Order object (2)>]> # it return all FRANK MPOYI order
>>>
>>> order = Order.objects.first()
>>> order.customer.name [variable.customerfilelofforeignkey.nameoffieldinCustomerclass]
'Frank Mpoyi'

>>> products = Product.objects.filter()
>>> products
<QuerySet [<Product: BBQ Grill>, <Product: Dishes>, <Product: Ball>]>

>>> products = Product.objects.filter(category="Out Door")
>>> products
<QuerySet [<Product: BBQ Grill>, <Product: Ball>]>

>>> products = Product.objects.all().order_by("id")
>>> products
<QuerySet [<Product: BBQ Grill>, <Product: Dishes>, <Product: Ball>]>

#reverse order
>>> products
<QuerySet [<Product: Ball>, <Product: Dishes>, <Product: BBQ Grill>]>
>>>

ManytoMany
>>> products = Product.objects.filter(tags__name="sport")
>>> products
<QuerySet [<Product: Ball>]>



RELATED SET EXEMPLE

class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    Parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)
    
parent = ParentModel.objects.first()
#Return all child models related to parent
parent.childmodel_set.all() # in related state we do with lowercase

'''