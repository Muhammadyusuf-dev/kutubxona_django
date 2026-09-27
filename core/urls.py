from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('mualliflar/', views.barcha_mualliflar, name='barcha_mualliflar'),
    path('muallif/<int:pk>/', views.muallif_detail, name='muallif_detail'),
    path('muallif/<int:pk>/ochirish/', views.muallif_ochirish, name='muallif_ochirish'),

    path('kitoblar/', views.barcha_kitoblar, name='barcha_kitoblar'),
    path('kitob/<int:pk>/', views.kitob_detail, name='kitob_detail'),

    path('recordlar/', views.barcha_recordlar, name='barcha_recordlar'),
    path('record/<int:pk>/', views.record_detail, name='record_detail'),
    path('record/<int:pk>/ochirish/', views.record_ochirish, name='record_ochirish'),

    path('talabalar/', views.barcha_talabalar, name='barcha_talabalar'),

    path('adminlar/', views.barcha_adminlar, name='barcha_adminlar'),

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