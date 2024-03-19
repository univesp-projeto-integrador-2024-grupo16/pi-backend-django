from django.urls import path, include
from rest_framework import routers

from qualificacao import views

app_name = 'qualificacao'

router = routers.DefaultRouter(
    trailing_slash=True
)

router.register(r'', views.UserViewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]