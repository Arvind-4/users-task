from django.urls import path
from user.views import create_user, get_users, delete_user, update_user

urlpatterns = [
    path("", create_user, name="create-user"),
    path("all/", get_users, name="get-users"),
    path("delete-user/", delete_user, name="delete-user"),
    path("update-user/", update_user, name="update-user"),
]
