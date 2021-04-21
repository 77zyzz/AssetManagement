from django.urls import path

from . import views

app_name = 'tools'
urlpatterns = [
    path('removesame/', views.removesame, name='removesame'),
]