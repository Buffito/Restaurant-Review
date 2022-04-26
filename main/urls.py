from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addrestaurant/', views.add_restaurant, name="add_restaurant"),
    path('editrestaurant/<int:id>/', views.edit_restaurant, name="edit_restaurant"),
    path('deleterestaurant/<int:id>/', views.delete_restaurant, name="delete_restaurant"),
]
