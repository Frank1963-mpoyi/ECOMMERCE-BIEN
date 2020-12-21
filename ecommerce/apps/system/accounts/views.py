from django.shortcuts import render, get_object_or_404, redirect
#import Django buidin Userregistration form 
#from django.contrib.auth.forms import UserCreationForm
#for logout to avoid anonymous user
from django.contrib.auth.decorators import login_required
from ecommerce.apps.system.authenticate.decorators   import  unauthenticated_user, allowed_users#, admin_only
from .models import Customer, Tag, Product, Order
#from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
#from django.contrib import messages
from ecommerce.apps.system.accounts.views import *







#we put decorator to the view we want to restricted
@login_required(login_url='login')
# it allowed only admin to login in home page
@allowed_users(allowed_roles=['admin'])#we can also pass multiple role like staff etc...
#@admin_only
def home (request):
    template_name       = 'accounts\dashboard.html'
    orders              = Order.objects.all()
    customers           = Customer.objects.all()
    
    total_customers     = customers.count()
    # total_customers = Customer.objects.all().count()
    
    total_orders        = orders.count()
    
    delivered           = orders.filter(status='Delivered').count()
    pending             = orders.filter(status='Pending').count()
    
    context             = {
        
        'orders'        : orders,
        'customers'     : customers,
        'total_orders'  : total_orders,
        'delivered'     : delivered,
        'pending'       : pending
        
    }   
    return render (request, template_name, context)




@login_required(login_url   ='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    template_name           = 'accounts/products.html'
    products                = Product.objects.all()
    context                 = {
        'products':products
    }
    return render (request, template_name, context )





@login_required(login_url   = 'login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk    = None):
    template_name           = 'accounts/customers.html'    
    #customer = Customer.objects.get(id =pk)
    customer                = get_object_or_404(Customer, id=pk)
    # Query customer order
    orders                  = customer.order_set.all()# orders = variable+querycustomerchildobject_set.all()
    
    order_count             = orders.count()
    
    #--------SEARCH--------------------
    myFilter                = OrderFilter(request.GET, queryset=orders)# is the orders variable above
    orders                  = myFilter.qs # remake the variable
    
    context                 = {
        'customer'          : customer,
        'orders'            : orders,
        'order_count'       :  order_count,
        'myFilter'          : myFilter 
        
    }   
    return render (request, template_name, context )


