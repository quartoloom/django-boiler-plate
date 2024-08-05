from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from accounts.models import User


class MyUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'phone', 'full_name', 'email', 'is_guest')
    list_filter = ('is_admin',)
    add_fieldsets = (
        (None, {'fields': ('username', 'phone', 'email', 'password1', 'password2', 'is_active', 'is_guest')}),
        ('Personal info', {'fields': ('full_name', 'gender', )}),
        ('Permissions', {'fields': ('is_admin', 'user_type')}),
    )
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'email', 'is_active', 'is_guest')}),
        ('Personal info', {'fields': ('full_name', 'gender', )}),
        ('Permissions', {'fields': ('is_admin', 'user_type')}),
    )

    search_fields = ('email', 'phone')
    ordering = ('phone', 'email', )
    filter_horizontal = ()


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)