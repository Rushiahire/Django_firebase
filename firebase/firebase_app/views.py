from django.shortcuts import render,redirect
from django.views import View
from .forms import SignInForm
import credentials



class Home(View):
    def get(self,request):
        
        return render(request,'base.html')
    
class SignIn(View):
    def get(self,request):
        content = {
            'page_title' : 'Sign in',
            'sign_in' : SignInForm()
        }
        return render(request,'sign_in_page.html',content)

    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        
        user = credentials.auth.create_user_with_email_and_password(email,password)
        print(user)

        return redirect('/')
    
    
class Login(View):
    def get(self,request):
        content={
            'page_title' : 'Login page',
            'login_form' : SignInForm()
        }        
        return render(request,"login_page.html",content)
    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        
        login = credentials.auth.sign_in_with_email_and_password(email,password)
        print(login)
        return redirect('/')
        


