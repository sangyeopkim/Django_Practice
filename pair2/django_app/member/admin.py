from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import MyUser


# class MyAdmin(UserAdmin):
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (_('Personal info'), {'fields': ('username', 'nickname', 'email')}),
    #     (_('Permissions'), {'fields': ('is_staff', 'is_superuser',
    #                                    'groups', 'user_permissions')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password1', 'password2'),
    #     }),
    # )


admin.site.register(MyUser)
