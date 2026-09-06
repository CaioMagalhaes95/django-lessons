
from django.urls import path

from . import views

urlpatterns = [
    
    path('music/', views.MusicList.as_view(), name='music-list'),
    path('music/<int:pk>', views.MusicDetail.as_view(), name='music-detail'),

    path('musician/', views.MusicianList.as_view(), name='musician-list'),
    path('musician/<int:pk>', views.MusicianDetail.as_view(), name='musician-detail'),

    path('instrument/', views.InstrumentList.as_view(), name='instrument-list'),
    path('instrument/<int:pk>', views.InstrumentDetail.as_view(), name='instrument-detail'),
]