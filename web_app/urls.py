from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tanecnici', views.tanecnici, name='tanecnici'),
   	path('tanecnik/<int:pk>', views.tanecnik, name='tanecnik'),
   	path('tanecnici_prehled', views.tanecnici_prehled, name='tanecnici_prehled'),
   	path('zavody_prehled', views.zavody_prehled, name='zavody_prehled'),
   	path('prihlasky_prehled/<int:pk>', views.prihlasky_prehled, name='prihlasky_prehled'),    
]
