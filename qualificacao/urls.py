from django.urls import path, include
from rest_framework import routers

from qualificacao import views

app_name = 'qualificacao'

router = routers.DefaultRouter(
    trailing_slash=True
)

router.register(r'fornecedor', views.FornecedorView, basename='fornecedor')
router.register(r'users', views.UserView, basename='users')
router.register(r'fornecedor_obras', views.FornecedorObraViewSet,basename='fornecedor_obras')
router.register(r'tipo_fornecimento',views.TipoFornecimentoViewSet, basename='tipo_fornecimento')
router.register(r'qualificacao', views.QualificacaoViewSet, basename='qualificacao')
router.register(r'obras_usuarios', views.ObrasUserView, basename='obra_usuario')

urlpatterns = [
    path('', include(router.urls)),
]