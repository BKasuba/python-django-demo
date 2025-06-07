from django.urls import path
from demo_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("database/", views.database, name="database")
]
