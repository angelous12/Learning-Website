from django.contrib import admin
from .models import UserCustom
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(UserCustom)
class UserCustomAdmin(UserAdmin):
   model = UserCustom
   fieldsets = (       
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','first_name', 'last_name','phone_number','phone_father','category','last_login','country','token','activeuser')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',
                                    'is_active', 'groups',
                                    'user_permissions')}),
    )
   add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'username',
                    'password1', 'password2')}
        ),
    )