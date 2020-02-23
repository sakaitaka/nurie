from django.contrib import admin
from django.urls import path
from django.urls import include
import file_upload.views as file_upload
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('success/url/', file_upload.success),
    path('', include('file_upload.urls')),
]
