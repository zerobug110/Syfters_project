from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('news', views.news, name="new"),
    path('contacts', views.contacts, name="contacts"),
    path('about', views.about, name="about"),
    path('product/<str:pk>', views.details, name="product")
]
