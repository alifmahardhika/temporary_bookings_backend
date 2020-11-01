from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserApi, SelfDetailsAPI
from knox import views as knox_views


urlpatterns = [
    path("api/v1/auth", include("knox.urls")),
    path("api/v1/auth/register", RegisterAPI.as_view()),
    path("api/v1/auth/login", LoginAPI.as_view()),
    path("api/v1/auth/user", UserApi.as_view()),
    path("api/v1/auth/logout", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("api/v1/user-details", SelfDetailsAPI.as_view()),
]