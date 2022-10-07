from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect("/")
        else:
        # Return an 'invalid login' error message.
            return render(request,'login.html')
        
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")

def register(request):
    if request.method == 'POST':
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       username=request.POST['username']
       email=request.POST['email']
       password1=request.POST['password1']
       password2=request.POST['password2']
       
       if password1==password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,'Username taken')
               return redirect('/register')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'Email taken')
               return redirect('/register')
           else:
               user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
               user.save()
               print('User Created')
       else:
           messages.info(request,'Password not matching')
           return redirect('/register')
       return redirect('/login')
    else:
       return render(request,'register.html')