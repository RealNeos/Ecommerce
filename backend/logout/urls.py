from django.urls import path
from .views import LogoutView

urlpatterns = [
    path('', LogoutView.as_view(), name='logout'),  # Logout API endpoint
]