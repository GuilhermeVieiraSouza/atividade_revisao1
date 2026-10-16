from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/<int:evento_id>/', views.detalhe, name='detalhe'),
    path('local/<int:local_id>/', views.local, name='local')
]