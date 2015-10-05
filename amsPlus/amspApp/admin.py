from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from amspApp.amspUser.models import MyUser

admin.site.register(MyUser,UserAdmin)
