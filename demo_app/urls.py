from django.urls import path
from demo_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("database/", views.database, name="database"),
    path("login/", auth_views.LoginView.as_view(template_name="demo_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", views.signup, name="signup"),
]
