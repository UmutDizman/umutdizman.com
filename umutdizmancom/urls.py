from django.urls import path
from . import views
from .views import *


app_name = "umutdizmancom"





urlpatterns = [
    
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("projects/", views.projects, name="projects"),
    path("about/", views.about, name="about"),
    path("hire-me/", views.hire_me, name="hire_me"),

    path("contact/", contact_view, name="contact"),
    path("contact/success/", contact_success_view, name="contact_success"),
    path("sitemap.xml", views.sitemap_view, name="sitemap"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
