from django.contrib import admin
from .models import EmpModel,DrgModel,DistModel,Users
# Register your models here.
admin.site.register(EmpModel)
admin.site.register(DrgModel)
admin.site.register(Users)
admin.site.register(DistModel)
class Media:
    js = (
        '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',  # jquery
        'js/admin.js',       # project static folder
    )