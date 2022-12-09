from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register,name="register"),
    path('employee/',views.employee,name="employee"),
    path('insertEmp/',views.insertEmp,name="insertEmp"),
    path('employee/editEmp/<int:e_id>',views.editEmp,name="editEmp"),
    path('updateEmp/<int:e_id>',views.updateEmp,name="updateEmp"),
    path('employee/deleteEmp/<int:e_id>',views.deleteEmp,name="deleteEmp"),
    path('distributor/',views.distributor,name="distributor"),
    path('insertDist/',views.insertDist,name="insertDist"),
    path('distributor/editDist/<int:dist_id>',views.editDist,name="editDist"),
    path('updateDist/<int:dist_id>',views.updateDist,name="updateDist"),
    path('distributor/deleteDist/<int:dist_id>',views.deleteDist,name="deleteDist"),
    path('drugs/',views.drugs,name="drugs"),
    path('drugs/deleteDrg/<int:dg_id>',views.deletedrg,name="deletedrg"),
    path('insertDrg/',views.insertDrg,name="insertDrg"),
    path('drugs/editDrg/<int:dg_id>',views.editDrg,name="editDrg"),
    path('updateDrg/<int:dg_id>',views.updateDrg,name="updateDrg"),
    path('user/',views.user,name="user"),
    path('bill/',views.bill,name="bill"),
    path('newBill/',views.newBill,name="newBill"),
    path('del_user/<str:username>',views.del_user,name="del_user"),
    path('updateUser/<str:username>',views.updateUser,name="updateUser"),
    path('editUser/<str:username>',views.editUser,name="editUser"),
    path('editEmp/<int:e_id>',views.editEmp,name="editEmp"),
    path('change_password/<str:username>',views.change_password,name="change_password")
    # path('drugs/editDrg/<int:dg_id>',views.editDrg)
    
]