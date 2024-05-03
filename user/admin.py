from django.contrib import admin
from user.models import User, Manager

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "full_name",
        "mob_num",
        "pan_num",
        "manager",
        "created_at",
        "updated_at",
        "is_active",
    ]
    list_per_page = 10


class ManagerAdmin(admin.ModelAdmin):
    list_display = ["manager_id", "manager_name", "is_active"]
    list_per_page = 10


admin.site.register(User, UserAdmin)
admin.site.register(Manager, ManagerAdmin)
