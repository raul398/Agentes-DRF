"""mav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apps.users.api.views.login import Login
from apps.users.api.views.logout import Logout
from apps.users.api.views.token_refresh import TokenRefreshAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agente/', include('apps.agentes.api.routers')),
    path('cpd/', include('apps.cpd.api.routers')),
    path('refresh-token/', TokenRefreshAPIView.as_view(), name = 'Token_refresh'),
    path('login/', Login.as_view(), name = 'Login'),
    path('logout/', Logout.as_view(), name = 'Logout'),
]
