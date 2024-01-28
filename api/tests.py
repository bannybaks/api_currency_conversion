import json

from django.test import TestCase
from django.urls import reverse


class CurrencyConvertionTests(TestCase):

    def test_get_exchange_rate_success(self):
        """Verifying that a request to a resource has been received.

        Returns status code 200 and whether there is an "exchange_rate" 
        field in the response data
        """
        response = self.client.get(reverse('get_current_usd'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('exchange_rate', data)

    def test_get_exchange_rate_failure(self):
        """Checking a request to a non-existent URL
        
        Returning a 404 status code.
        """
        response = self.client.get(reverse('get_current_usd') + 'nonexistent/')
        self.assertEqual(response.status_code, 404)

    def test_latest_requests_limit(self):
        """Check limit on write restriction
        
        The limit in 10 records of the latest requests
        """
        for _ in range(15):
            response = self.client.get(reverse('get_current_usd'))
            self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('get_current_usd'))
        data = json.loads(response.content)
        self.assertEqual(len(data['latest_requests']), 10)