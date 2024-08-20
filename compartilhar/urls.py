from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.listar_arquivos, name='listar_arquivos'),
    path('baixar/<int:arquivo_id>/', views.baixar_arquivo, name='baixar_arquivo'),
    path('upload/', views.upload_arquivo, name='upload_arquivo'),
    path('excluir/<int:arquivo_id>/', views.excluir_arquivo, name='excluir_arquivo'),
]
