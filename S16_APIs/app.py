import requests

APP_ID = 'be72c8550b30432296ba5e8fe9618124'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
exchange_rates = response.json()['rates']

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['GBP']

print(gbp_amount)