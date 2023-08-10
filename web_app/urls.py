from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('kluby_prehled', views.kluby_prehled, name='kluby_prehled'),
    path('klub', views.klub, name='klub'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('tanecnici', views.tanecnici, name='tanecnici'),
   	path('tanecnik/<int:pk>', views.tanecnik, name='tanecnik'),
   	path('tanecnici_prehled', views.tanecnici_prehled, name='tanecnici_prehled'),
   	path('zavody_prehled', views.zavody_prehled, name='zavody_prehled'),
   	path('prihlasky_prehled/<int:pk>', views.prihlasky_prehled, name='prihlasky_prehled'),    
   	path('pridat_tanecnika', views.pridat_tanecnika, name='pridat_tanecnika'),
   	path('upravit_tanecnika/<int:pk>', views.upravit_tanecnika, name='upravit_tanecnika'),
   	path('smazat_tanecnika/<int:pk>', views.smazat_tanecnika, name='smazat_tanecnika'),
   	path('tanecni_jednotky_prehled', views.tanecni_jednotky_prehled, name='tanecni_jednotky_prehled'),
   	path('tanecni_jednotka/<int:pk>', views.tanecni_jednotka, name='tanecni_jednotka'),
   	path('pridat_tj/<int:pk>', views.pridat_tj, name='pridat_tj'),
   	path('upravit_tj/<int:pk>', views.upravit_tj, name='upravit_tj'),
   	path('smazat_tj/<int:pk>', views.smazat_tj, name='smazat_tj'),
]
