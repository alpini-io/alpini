from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'paginaname': ''}, name='pagine'),
    path('contatto', views.contatto, name='contatto'),
    path('<str:paginaname>',views.index, name='index')
]