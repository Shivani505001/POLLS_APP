#manages all urls for the project. The mysite.urls module is created by default with the command startproject. It’s a normal Python module with module-level variables representing Django URL patterns. Django will look for this module using import_module().

"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from django.conf.urls import include,url
from django.urls import path,include


#we have to connnect url.py with views.py
#connect url.py in mysite with views.py in polls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls',namespace='polls')),#namespace is used to differentiate between urls of different apps 
]
