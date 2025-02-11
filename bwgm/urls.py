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
