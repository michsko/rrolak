from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tanecnici', views.tanecnici, name='tanecnici'),
   	path('tanecnik/<int:pk>', views.tanecnik, name='tanecnik'),
    
]
