from django.contrib import admin
from django.urls import path

# main ilovasidan views ni chaqirib olamiz
from main import views

urlpatterns = [

    # Hamma ro'yxatlar
    path('mualliflar/', views.barcha_mualliflar, name='barcha_mualliflar'),
    path('kitoblar/', views.barcha_kitoblar, name='barcha_kitoblar'),
    path('recordlar/', views.barcha_recordlar, name='barcha_recordlar'),

    # Detail (Bitta ob'ekt) sahifalari
    path('muallif/<int:pk>/', views.muallif_detail, name='muallif_detail'),
    path('kitob/<int:pk>/', views.kitob_detail, name='kitob_detail'),
    path('record/<int:pk>/', views.record_detail, name='record_detail'),

    # Maxsus so'rovlar (Filtrlanganlar)
    path('mualliflar/tirik/', views.tirik_mualliflar, name='tirik_mualliflar'),
    path('kitoblar/top-sahifa/', views.top_sahifali_kitoblar, name='top_sahifali_kitoblar'),
    path('mualliflar/top-kitob/', views.top_kitobli_mualliflar, name='top_kitobli_mualliflar'),
    path('recordlar/oxirgi/', views.oxirgi_recordlar, name='oxirgi_recordlar'),
    path('kitoblar/tirik-muallif/', views.tirik_muallif_kitoblari, name='tirik_muallif_kitoblari'),
    path('kitoblar/badiiy/', views.badiiy_kitoblar, name='badiiy_kitoblar'),
    path('mualliflar/yoshi-katta/', views.yoshi_katta_mualliflar, name='yoshi_katta_mualliflar'),
    path('kitoblar/kam-kitobli-muallif/', views.kam_kitobli_muallif_kitoblari, name='kam_kitobli_muallif'),
    path('recordlar/bitiruvchi/', views.bitiruvchi_recordlari, name='bitiruvchi_recordlari'),
]