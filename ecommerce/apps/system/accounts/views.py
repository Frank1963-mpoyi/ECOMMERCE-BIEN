from django.shortcuts import render, get_object_or_404, redirect

#import Django buidin Userregistration form 
from django.contrib.auth.forms import UserCreationForm

from .models import Customer, Tag, Product, Order
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout




def registerPage(request):
    template_name = "accounts/register.html"
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            #just to get a user name to display in the message
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('login')
    context ={
        'form': form
    }
    return render (request, "accounts/register.html", context)


def loginPage(request):
    if request.method == "POST":
        # let grap username and password from userin frontend
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #after getting username and password let authenticate
        user = authenticate(request, username=username, password=password)
        #before authenticate let check if user is there
        if user is not None:
            login(request, user)#we will login this user
            return redirect('home')
        else:
            messages.info(request, "Username OR Passowrd is incorrect")
    
    template_name = "accounts/login.html"
    context = {
        
    }
    return render (request,template_name, context)

def logoutUser(request):
    logout(request)
    return redirect ("login")




def home (request):
    orders          = Order.objects.all()
    customers       = Customer.objects.all()
    
    total_customers = customers.count()
    # total_customers = Customer.objects.all().count()
    
    total_orders    = orders.count()
    
    delivered       = orders.filter(status='Delivered').count()
    pending         = orders.filter(status='Pending').count()
    
    context         = {
        
        'orders'        : orders,
        'customers'     : customers,
        'total_orders'  : total_orders,
        'delivered'     : delivered,
        'pending'       : pending
        
    }
    template_name    = 'accounts\dashboard.html'
    
    return render (request, template_name, context)



def products(request):
    template_name   = 'accounts/products.html'
    products        = Product.objects.all()
    context = {
        'products':products
    }
    return render (request, template_name, context )



def customer(request, pk=None):
    
    #customer = Customer.objects.get(id =pk)
    customer        = get_object_or_404(Customer, id=pk)
    # Query customer order
    orders          = customer.order_set.all()# orders = variable+querycustomerchildobject_set.all()
    
    order_count     = orders.count()
    
    #--------SEARCH--------------------
    myFilter        = OrderFilter(request.GET, queryset=orders)# is the orders variable above
    orders          = myFilter.qs # remake the variable
    
    context         = {
        'customer'  : customer,
        'orders'    : orders,
        'order_count':  order_count,
        'myFilter'    : myFilter 
        
    }
    template_name   = 'accounts/customers.html'
    
    return render (request, template_name, context )

def createOrder(request):
    
    form = OrderForm()
    if request.method == 'POST':
    #print("Printing POST:", request.POST) this will print data in the same page
        form = OrderForm(request.POST)# we can pass the data in the form
        if form.is_valid():
            form.save()
            return redirect("/")# empty mean main template
    
    template_name = "accounts/order_form.html"
    context ={
        'form': form
    }
    return render (request, template_name, context)

def updateOrder(request, pk=None):
    template_name = "accounts/order_form.html"
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {
        'form': form
    }       
    return render (request, template_name, context)

def deleteOrder(request, pk=None):
    template_name = 'accounts/delete.html'
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context ={
        'item': order
    }
    
    return render (request, template_name, context)