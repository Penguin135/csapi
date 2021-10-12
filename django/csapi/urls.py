from django.urls import path
from . import views

app_name = 'csapi'

urlpatterns = [
    path('', views.index),
    path('upload/', views.upload, name='upload'),
    path('origin-images/<int:image_id>/', views.origin_image_show, name='origin_image_show'),
]
