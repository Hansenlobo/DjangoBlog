from django.urls import path,include
from . import views


urlpatterns = [
        path('', views.allblogs, name='allblogs'),
        path('search/', views.search, name='search'),
        path('<slug:post>/', views.detail, name="detail"),
]
