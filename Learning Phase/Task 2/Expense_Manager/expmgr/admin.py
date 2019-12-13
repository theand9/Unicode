from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.loginDetails)
admin.site.register(models.userInfo)
admin.site.register(models.userAcc)
admin.site.register(models.incomeStream)
admin.site.register(models.Expenses)
