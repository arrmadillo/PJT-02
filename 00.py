import requests
from pprint import pprint

order_currency = "BTC"
payment_currency = "KRW"
url = f"https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}"

res = requests.get(url=url).json()
data = res["data"]
answer = int(data['prev_closing_price']) # 전일 종가 저장
pprint(answer)