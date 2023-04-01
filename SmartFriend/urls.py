from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth_app.urls')),
    path('openai/', include('open_ai.urls')),
    path('admin/', admin.site.urls),
]