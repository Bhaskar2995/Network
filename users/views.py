from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
from django.views import View
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    def post(Self,request,*args,**kwargs):
        print('testing in loginview post')
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print(user_name)
        print(password)
        user = authenticate(email=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            message="Invalid Credentials !!!"
            success=False
        return render(request,'login.html',{'message':message,'success':success})
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('/')
    
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'register.html')
    def post(Self,request,*args,**kwargs):
        User = get_user_model()
        email=request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password!=confirm_password:
            message="password and confirm password is not matching"
            return render(request,'register.html',{'message':message})
        user=User.objects.create(email=email,password=password)
        user.save()
        return redirect('/')


