from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('item/<int:item_id>/', views.show_item, name='show_item'),
    path('items/', views.item_list, name='item_list'),
]
