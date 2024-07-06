"""
URL configuration for Getentity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path


from EntityById import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abc/',views.get_homepath, name='get_homepath'),
    path('getentitybyid/<int:id>/', views.get_entity, name='get_entity'),
    path('getentities', views.get_entities, name='get_entities'),
    path('getentitiesbynaturalsource/<str:natural_source>/', views.get_entity_by_natural_source, name='get_entity_by_natural_source'),
    path('entityautocomplete', views.entity_autocomplete, name='entity_autocomplete'),
]

