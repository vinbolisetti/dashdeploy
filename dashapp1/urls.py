from . import views
from django.urls import path


urlpatterns = [
    path('app1/', views.app1, name='app1')
]