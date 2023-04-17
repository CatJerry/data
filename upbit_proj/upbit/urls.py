from django.urls import path    
from upbit import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_coin_data/', views.get_coin_data, name='get_coin_data'),
]
