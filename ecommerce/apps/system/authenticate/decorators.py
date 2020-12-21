from django.http import HttpResponse
from django.shortcuts import redirect

'''
@unauthenticated_user
def loginPage(request): # the loginPage will pass in view_func, now view_func is now loginPage
    pass
'''


def unauthenticated_user(view_func):
    #we need to make the in function like nested function
    #a decoration is a function that take another function in as a parameter
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists(): # if the user is in the group
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorise to view this page')
                
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator




    def admin_only(view_func):
        def wrapper_function(request, *args, **kwargs):            
            group = None
            if request.user.groups.exists(): # if the user is in the group
                group = request.user.groups.all()[0].name
            # dont do this in real project    
            if group == 'customer':
                return redirect('user-page')
            
            if group =='admin':
                return view_func(request, *args, **kwargs)
        
        return wrapper_function
    