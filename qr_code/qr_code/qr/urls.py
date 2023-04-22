from django.urls import path
from .views import qr_codes

urlpatterns = [
    path('' , qr_codes , name="qr_codes_page")
]