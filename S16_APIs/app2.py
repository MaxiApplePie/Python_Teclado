import time
from libs.openexchange import OpenExchangeClient

APP_ID = 'be72c8550b30432296ba5e8fe9618124'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount, 'EUR', 'GBP')
end = time.time()

print(end - start)

start = time.time()
gbp_amount = client.convert(usd_amount, 'EUR', 'GBP')
end = time.time()

print(end - start)

start = time.time()
gbp_amount = client.convert(usd_amount, 'EUR', 'GBP')
end = time.time()

print(end - start)



print(f'USD {usd_amount} is GBP {gbp_amount:.2f}')

