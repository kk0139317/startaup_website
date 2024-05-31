from django.urls import path, include
from userpannel import views
urlpatterns = [
    path("", views.HomePage, name="Homepage"),
    path("index", views.HomePage, name="Homepage"),
    path("about", views.AboutUs, name="ABout Us Page"),
    path('service', views.ServicePage, name="Service Page"),
    path('contact', views.Contact, name="Contact Page"),
    path('team', views.Team, name="Team Page"),
    path('blog', views.Blog, name="BLog Page"),
    path('detail', views.Detail, name="detail"),
]
