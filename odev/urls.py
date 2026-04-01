from django.urls import path
from .views import ana_sayfa

urlpatterns = [
    path('', ana_sayfa), # Boş tırnak 'ana sayfa' demek
]