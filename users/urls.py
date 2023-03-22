from django.urls import path

from users.views import UserRegister,UserListView

urlpatterns = [
    path("users/register/", UserRegister.as_view(), name='register'),
    path("api/users/list", UserListView.as_view(), name="user-list"),
]
