"""shakespeare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),

    # Now home directs to our index:
    url(r'^$', include('shakespeareapp.urls')),
    # Interesting, it's still listening on /shakespeareapp...Something to do with regex -- it's accepting anything ending in 'app'!:
    url('app/', include('shakespeareapp.urls'))
]

#
# urlpatterns = [
#     url('admin/', admin.site.urls),
#     url('todos/', include('todos.urls')),
#     # url('cityname/', include('cityname.urls')),
#
#     url(r'^$', include('todos.urls')),
#
# ]
