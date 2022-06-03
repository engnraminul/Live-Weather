from django.urls import path
from .import views
app_name='Weather'
urlpatterns = [
    path('weather/', views.weather),
]
