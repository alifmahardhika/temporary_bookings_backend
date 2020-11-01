from django.contrib import admin
from .models import JBIDetails, UserDetails
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.


class UserDetailsInline(admin.StackedInline):
    model = UserDetails
    can_delete = False
    verbose_name_plural = "userdetails"


class UserAdmin(BaseUserAdmin):
    inlines = (UserDetailsInline,)


class JBIDetailsAdmin(admin.ModelAdmin):
    fields = ("nama_lembaga", "email_lembaga", "diluar_jadwal", "is_nonactive")
    list_display = (
        "nama_lembaga",
        "email_lembaga",
        "diluar_jadwal",
        "is_nonactive",
        "last_updated",
    )


class UserDetailsAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "is_activated",
        "role",
        "phone",
        "gender",
        "user_photo",
    )
    list_display = (
        "user",
        "is_activated",
        "role",
        "phone",
        "gender",
        "last_updated",
    )


admin.site.register(JBIDetails, JBIDetailsAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserDetails, UserDetailsAdmin)
