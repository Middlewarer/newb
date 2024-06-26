from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('home/', views.DefaultView.as_view(), name='home'),
    path('create/', views.TicketCreateView.as_view(), name='create'),
    path('tickets/', views.TicketListView.as_view(), name='ticket_list'),
    path('api/', views.table_api, name='api'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit/', views.UserProfileUpdateView.as_view(), name='edit'),
    path('appi/', views.user_tickets_api, name='appi'),
    path('apppi/', views.user_new_tickets_api, name='apppi'),
    path('ticket_detail/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
]