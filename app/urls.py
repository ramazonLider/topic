from django.urls import path
from .views import home, detail, search

urlpatterns = [
    path('', home, name="home"),
    path('topic/<int:id>', detail, name="detail"),
    path('search/', search, name="search")
]
