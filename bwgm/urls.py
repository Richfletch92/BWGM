"""
URL configuration for bwgm project.

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
from django.urls import path, include

urlpatterns = [
    # Include allauth URLs for account management (registration, login, etc.)
    path('accounts/', include('allauth.urls')),
    # Admin site URL
    path('admin/', admin.site.urls),
    # Include django_summernote URLs for the Summernote WYSIWYG editor
    path('summernote/', include('django_summernote.urls')),
    # Include URLs from the home app
    path('', include('home.urls')),
]
