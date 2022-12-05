from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'hour'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('detail_day/<int:day_id>/', views.DetailDay.as_view() , name='detail_day'),
    path('overview.txt', TemplateView.as_view(template_name='hour/overview.txt', content_type='text/plain')),

    path('delete_day/<int:day_id>/', views.DeleteDay.as_view() , name='delete_day'),
    path('update_day/<int:day_id>/', views.UpdateDay.as_view() , name='update_day'),
]