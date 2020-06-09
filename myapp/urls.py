"""teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.responseform),
    path('', views.home),
    path('param/', views.responseform),
    path('thankyou/', views.responseform),
    # path('manualparam/', views.serialform),
    # path('manualok/', views.serialform),

    # path('external', views.external),
    # # path('your-name',views.NameForm),
    # path('output', views.output, name="script"),

    
]
