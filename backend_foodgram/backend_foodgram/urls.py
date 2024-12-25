from api.views import load_url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('s/<str:url_hash>/', load_url, name='load_url'),
]
