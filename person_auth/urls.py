from . import views
from django.urls import path

app_name = 'person_auth'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('post_create', views.post_create, name='post_create'),

]