
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('exam.exam_notes.urls')),
    path('profile/',include('exam.exam_profile.urls')),
]
