from django.contrib import admin
from .models import EmpModel,DrgModel,DistModel
# Register your models here.
admin.site.register(EmpModel)
admin.site.register(DrgModel)
admin.site.register(DistModel)