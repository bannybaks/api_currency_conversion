from datetime import datetime
import logging
import requests
import time

import pytz

from django.views import View
from django.http import JsonResponse


logger = logging.getLogger(__name__)

class CurrencyConvertion(View):
    USD_RUB_API_URL = "https://open.er-api.com/v6/latest/USD"
    latest_requests = []

    def get_exchange_rate(self):
        try:
            response = requests.get(self.USD_RUB_API_URL)
            response.raise_for_status()
            data = response.json()
            return data['rates']['RUB']
        except requests.RequestException as error:
            logger.error(f'Error fetching exchange rate: {error}')
            return None
    
    def add_request(self, exchange_rate):
        current_time_utc = datetime.utcnow()
        utc_timezone = pytz.timezone('UTC')
        local_timezone = pytz.timezone('Europe/Moscow')

        current_time_utc = utc_timezone.localize(current_time_utc)
        current_time_local = current_time_utc.astimezone(local_timezone)
        formatted_request = {
            'date': current_time_local.strftime('%Y-%m-%d'),
            'time': current_time_local.strftime('%H:%M:%S'),
            'exchange_rate': exchange_rate
        }
        self.latest_requests.insert(0, formatted_request)
        if len(self.latest_requests) > 10:
            self.latest_requests = self.latest_requests[-10:]
    
    def get(self, request):
        exchange_rate = self.get_exchange_rate()
        if exchange_rate is not None:
            self.add_request(exchange_rate)
            time.sleep(10)
            logger.info('Data received on the dollar to ruble exchange rate')
            return JsonResponse({
                'exchange_rate': {'RUB': exchange_rate},
                'latest_requests': self.latest_requests
            })
        else:
            logger.exception('Failed to fetch exchange rate')
            return JsonResponse(
                {'error': 'Failed to fetch exchange rate'},
                status=500
            )
