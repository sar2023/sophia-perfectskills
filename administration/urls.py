from django.urls import path
from administration.views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',staffLogin,name='staffLogin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('allAnswer/',allAnswer,name='allAnswer'),
    path('searchbar/',searchbar,name='searchbar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)