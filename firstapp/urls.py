
from django.urls import path
from . import views
urlpatterns = [
    path('demo', views.demo,name='demo'),
    path('country/', views.country,name='country'),
    path('provience/', views.provience,name='provience')
]
