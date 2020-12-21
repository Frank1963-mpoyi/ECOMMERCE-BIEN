from django.shortcuts                       import render
from ecommerce.apps.system.accounts.models  import      *

#from ecommerce.apps.system.authenticate.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from ecommerce.apps.system.authenticate.decorators   import  unauthenticated_user, allowed_users#, admin_only
from ecommerce.apps.system.accounts.forms  import OrderForm
from ecommerce.apps.system.accounts.views  import * # for delete redirect home


@login_required(login_url   ='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request):
    template_name           = "blog/order_form.html"
    form                    = OrderForm()
    if request.method       == 'POST':
    #print("Printing POST:", request.POST) this will print data in the same page
        form                = OrderForm(request.POST)# we can pass the data in the form
        if form.is_valid():
            form.save()
            return redirect("/")# empty mean main template    
    context                 = {
        'form'              : form
    }
    return render (request, template_name, context)





@login_required(login_url   = 'login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk = None):
    template_name           = "blog/order_form.html"
    
    order                   = Order.objects.get(id=pk)
    form                    = OrderForm(instance=order)
    
    if request.method       == 'POST':
        form                = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context                 = {
        'form': form
    }       
    return render (request, template_name, context)




@login_required(login_url   = 'login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk = None):
    template_name           = 'blog/delete.html'
    order                   = Order.objects.get(id=pk)
    if request.method       == "POST":
        order.delete()
        return redirect('/')
    
    context                 = {
        'item': order
    }   
    return render (request, template_name, context)