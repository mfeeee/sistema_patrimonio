"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import lista_patrimonio, novo_patrimonio, editar_patrimonio, deletar_patrimonio
from usuarios.views import registrar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', registrar_usuario, name='registrar_usuario'),

    path('', lista_patrimonio, name='lista_patrimonio'),
    path('novo/', novo_patrimonio, name='novo_patrimonio'),
    path('editar/<int:id>/', editar_patrimonio, name='editar_patrimonio'), 
    path('deletar/<int:id>/', deletar_patrimonio, name='deletar_patrimonio'),
]
