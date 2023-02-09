"""show_route URL Configuration

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
from django.urls import path

from route.views import showroute,showmap,home,reports,showreport,connect_ais_stream

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showroute/',showroute,name='showroute'),
    path('showreport/',showreport,name='showreport'),
    path('showmap/',showmap,name='showmap'),
    path('reports/',reports,name='reports'),
    path('get_real_time_ships/',connect_ais_stream,name='get_real_time_ships'),
    path('',home,name='home'),

    ]
