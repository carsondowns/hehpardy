from django.urls import path

from .views import index


app_name = 'pardy'

urlpatterns = [
    path('', index, name='index'),
]