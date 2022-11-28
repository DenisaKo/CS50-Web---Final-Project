from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'hours'

urlpatterns = [
    path('', views.index, name='index'),
    path('overview.txt', TemplateView.as_view(template_name='overview.txt', content_type='text/plain')),
    # path('login', views.login_view, name='login'),
    # path('logout', views.logout_view, name='logout'),
    # path('register', views.register, name='register'),

    # API
    path('get_days', views.get_days, name='get_days'),
]