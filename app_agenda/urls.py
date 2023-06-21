
from app_agenda import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', views.salvar, name='salvar' ),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('meusdados', views.meusdados, name='meusdados')
    
]