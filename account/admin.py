from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm
from .models import Account
from django.contrib.auth.models import Group
from .forms import AccountChangeForm, AccountCreationForm

class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm

    list_display = ('email', 'name', 'profile_image', )
    search_fields = ('email', 'name')
    readonly_fields = ('last_login', 'date_joined', 'is_superuser', 'is_admin')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'name', 'profile_image','password')}),
        ('Permissions', {'fields': ('is_admin',)})
    )
    ordering = ('email',)
    add_fieldsets = ((None, {'classes': ('wide',),'fields': ('email', 'name', 'profile_image', 'password1', 'password2'),}),)

admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)