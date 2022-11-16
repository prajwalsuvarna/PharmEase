from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from members.models import EmpModel
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
def employee(request):
    if request.user.is_anonymous:
        return redirect("/login")
    showAll=EmpModel.objects.all
    return render(request,'employee.html',{'data':showAll})   
     
def insertEmp(request):
    if request.method=='POST':
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('e_id'):
            saverecord=EmpModel()
            saverecord.e_id=request.POST.get('e_id')
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.mobile=request.POST.get('mobile')
            saverecord.save()
            messages.success(request,'Employee '+saverecord.empname+' is saved successfully!')
            return render(request,'insertEmp.html')
    else:
            return render(request,'insertEmp.html')
    
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

# edit Employee details
def editEmp(request,e_id):
    editEmpObj=EmpModel.objects.get(e_id=e_id)
    return render(request,'editEmp.html',{"EmpModel":editEmpObj})