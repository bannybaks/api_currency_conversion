from django.urls import path
from .views import CurrencyConvertion

urlpatterns = [
    path(
        'get-current-usd/',
        CurrencyConvertion.as_view(),
        name='get_current_usd'
    ),
]
