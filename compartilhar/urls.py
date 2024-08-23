from django.urls import path, include
from .views import ArquivoViewSet, listar_arquivos, baixar_arquivo, upload_arquivo, excluir_arquivo
from rest_framework.routers import DefaultRouter

# Configurar o router para as rotas da API REST
router = DefaultRouter()
router.register(r'arquivos', ArquivoViewSet)

urlpatterns = [
    # URLs para o site
    path('', listar_arquivos, name='listar_arquivos'),
    path('baixar/<int:arquivo_id>/', baixar_arquivo, name='baixar_arquivo'),
    path('upload/', upload_arquivo, name='upload_arquivo'),
    path('excluir/<int:arquivo_id>/', excluir_arquivo, name='excluir_arquivo'),

    # URLs para a API REST
    path('api/', include(router.urls)),
]
