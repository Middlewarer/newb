from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('default/', views.default, name='default'),
    path('create/', views.create_ticket, name='create'),

]