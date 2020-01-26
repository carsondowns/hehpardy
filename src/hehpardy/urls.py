from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pardy/', include('pardy.urls', namespace='pardy')),
]