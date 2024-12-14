"""
Register the models to django admin
"""
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from core import models


class UserAdmin(BaseUserAdmin):
    """Register the users model to django admin"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None,
         {'fields':
              ('email', 'password')
          }
         ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        ('Important dates',
         {'fields':
              ('last_login',)
          }
         ),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None,{
             'fields':
                 (
                     'email',
                     'password',
                     'password2',
                     'name',
                     'is_active',
                     'is_staff',
                     'is_superuser',
                 )
         }
         ),
    )


admin.site.register(models.User, UserAdmin)
