from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from members.models import EmpModel, DistModel, DrgModel, Bill
from django.db.models import Max
from datetime import datetime
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

# Create your views here.


def index(request):
    showAll = EmpModel.objects.all()
    emp_count = showAll.count()
    showAll = DistModel.objects.all()
    dist_count = showAll.count()
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html', {'emp_count': emp_count, 'dist_count': dist_count})


def employee(request):
    if request.user.is_anonymous:
        return redirect("/login")
    showAll = EmpModel.objects.all()
    return render(request, 'employee.html', {'data': showAll})


def distributor(request):
    if request.user.is_anonymous:
        return redirect("/login")
    showAll = DistModel.objects.all()
    return render(request, 'dist.html', {'data': showAll})


def drugs(request):
    if request.user.is_anonymous:
        return redirect("/login")
    showAll = DrgModel.objects.all()
    return render(request, 'drug.html', {'data': showAll})


def user(request):
    if request.user.is_anonymous:
        return redirect("/login")
    showAll = User.objects.all()
    showAll1 = EmpModel.objects.all()
    return render(request, 'user.html', {'data': showAll, 'data1': showAll1})


def insertEmp(request):
    e_id = 1001 if EmpModel.objects.count(
    ) == 0 else EmpModel.objects.aggregate(max=Max('e_id'))["max"]+1
    saverecord = EmpModel()
    if request.method == 'POST':
        saverecord.e_id = e_id
        saverecord.empname = request.POST.get('empname')
        saverecord.email = request.POST.get('email')
        saverecord.mobile = request.POST.get('mobile')
        saverecord.save()
        messages.success(request, 'Employee ' +
                         saverecord.empname+' is saved successfully!')
        return render(request, 'insertEmp.html')
    else:
        return render(request, 'insertEmp.html')


def insertDist(request):
    dist_id = 401 if DistModel.objects.count(
    ) == 0 else DistModel.objects.aggregate(max=Max('dist_id'))["max"]+1
    saverecord = DistModel()
    if request.method == 'POST':
        saverecord.dist_id = dist_id
        saverecord.dist_name = request.POST.get('dist_name')
        saverecord.d_email = request.POST.get('d_email')
        saverecord.d_pno = request.POST.get('d_pno')
        saverecord.save()
        messages.success(request, 'Distributor  ' +
                         saverecord.dist_name+' is saved successfully!')
        return render(request, 'insertDist.html')
    else:
        return render(request, 'insertDist.html')


def insertDrg(request):
    dg_id = 120 if DrgModel.objects.count(
    ) == 0 else DrgModel.objects.aggregate(max=Max('dg_id'))["max"]+1
    saverecord = DrgModel()
    showAll = DistModel.objects.all()
    print(showAll)
    if request.method == 'POST':
        print(request.POST)
        saverecord.dg_id = dg_id

        saverecord.dgname = request.POST.get('dgname')
        saverecord.stock = request.POST.get('stock')
        saverecord.price = request.POST.get('price')
        saverecord.dist_id_id = request.POST.get('dist_id')
        saverecord.save()
        messages.success(request, 'Distributor  ' +
                         saverecord.dgname+' is saved successfully!')
        return render(request, 'insertDrg.html', {"data": showAll})
    else:
        return render(request, 'insertDrg.html', {"data": showAll})


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
        else:
            messages.info(request, 'Password not matching')
            return redirect('/register')
        return redirect('/login')
    else:
        return render(request, 'register.html')

# edit Employee details


def editEmp(request, e_id):
    editEmpObj = EmpModel.objects.get(e_id=e_id)
    return render(request, 'editEmp.html', {"EmpModel": editEmpObj})


def updateEmp(request, e_id):
    updateEmp = EmpModel.objects.get(e_id=e_id)
    if request.method == 'POST':
        updateEmp.empname = request.POST.get('empname')
        updateEmp.email = request.POST.get('email')
        updateEmp.mobile = request.POST.get('mobile')
        updateEmp.save()
        messages.success(request, 'Employee ' +
                         updateEmp.empname+' is updated successfully!')
        print(messages)
        return render(request, 'editEmp.html', {"EmpModel": updateEmp})


def editDist(request, dist_id):
    editDistObj = DistModel.objects.get(dist_id=dist_id)
    return render(request, 'editDist.html', {"DistModel": editDistObj})


def updateDist(request, dist_id):
    updateDist = DistModel.objects.get(dist_id=dist_id)
    if request.method == 'POST':
        updateDist.dist_name = request.POST.get('dist_name')
        updateDist.d_email = request.POST.get('d_email')
        updateDist.d_pno = request.POST.get('d_pno')
        updateDist.save()
        messages.success(request, 'Distributor' +
                         updateDist.dist_name+' is updated successfully!')
        print(messages)
        return render(request, 'editDist.html', {"DistModel": updateDist})


def deleteDist(self, dist_id):
    delDist = DistModel.objects.filter(dist_id=dist_id)
    delDist.delete()
    return redirect('/distributor')


def deleteEmp(self, e_id):
    delEmployee = EmpModel.objects.filter(e_id=e_id)
    delEmployee.delete()
    return redirect('/employee')


def bill(request):
    sale_id = 1900 if Bill.objects.count() == 0 else Bill.objects.aggregate(
        max=Max('sale_id'))["max"]+1
    print(sale_id)
    data1 = sale_id
    if request.user.is_anonymous:
        return redirect("/login")
    showAll = Bill.objects.all()
    return render(request, 'bill.html', {'data': showAll, 'data1': data1})


def newBill(request):
    sale_id = 1900
    print(sale_id)
    showAll2 = DrgModel.objects.all()
    saverecord = Bill()
    if request.method == 'POST':
        print(request.POST)
        a = request.POST.get('drg_id')
        d1 = DrgModel.objects.get(dg_id=a)
        saverecord.sale_id = sale_id
        saverecord.cname = request.POST.get('cname')
        saverecord.age = request.POST.get('age')
        saverecord.phone_no = request.POST.get('phone_no')
        saverecord.stock = request.POST.get('stock')
        saverecord.emp_name = str(request.user)
        print(d1.price)
        print(saverecord.stock)
        saverecord.amt = int(saverecord.stock) * int(d1.price)
        print(saverecord.amt)
        print(request.user)
        saverecord.save()

        saverecord.drg_id.add(d1)
        print(saverecord)
        # messages.success(request,'  '+saverecord.drg_id+' is saved successfully!')
        return render(request, 'newBill.html', {"data": showAll2, })
    else:
        return render(request, 'newBill.html', {"data": showAll2, "sale_id": sale_id})
