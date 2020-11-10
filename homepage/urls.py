from django.urls import path
from . import views

urlpatterns = [
    path('api/data/', views.save_data.as_view())
]