from django.contrib import admin
from django.urls import path, include
from escola.views import AunosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', AunosViewSet)

#criando as rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
