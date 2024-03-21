from django.urls import path, include
from rest_framework import routers

from qualificacao import views

app_name = 'qualificacao'

router = routers.DefaultRouter(
    trailing_slash=True
)

router.register(r'fornecedor', views.FornecedorView, basename='fornecedor')

urlpatterns = [
    path('', include(router.urls)),
]