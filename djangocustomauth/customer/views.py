from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout 
from core.decorators import login_and_role_required  

@login_and_role_required("customer")
def customer_dashboard_view(request):
    return render(request,'customer/dashboard.html')

@login_and_role_required("customer")
def password_change_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(
                request,"Password change successfully!! Please login with your new password"
            )
            return redirect('login')
        else:
            #handle form errors and display them to the user
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request,error) 
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'customer/password_change.html',{'form':form})