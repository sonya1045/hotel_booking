from django.urls import path
from auth_system import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_views, name="login"),
    path("logout/", views.logout_views, name="logout"),
]