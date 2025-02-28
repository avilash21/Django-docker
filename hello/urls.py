from django.urls import path
from hello import views

urlpatterns = [
    path('', views.redirectview, name='redirect-view'),  # Root URL redirects to /redirect/
    path('home/', views.homeview, name='home-view'),  # /redirect/ goes to Google
]
