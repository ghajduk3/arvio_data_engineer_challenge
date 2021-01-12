from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('display',views.get_certificate,name='get_certificate'),
    path('fillData',views.insert_data_db,name='insert_data_db'),
]