from django.urls import path

from exam.exam_profile.views import profile_page, create_profile, delete_user

urlpatterns = [
    path('',profile_page, name='profile page'),
    path('create/',create_profile, name='create profile'),
    path('delete_user/',delete_user,name = 'delete user')
]