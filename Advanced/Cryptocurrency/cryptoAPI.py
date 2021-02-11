import requests
import json

key = '<your_key>'

url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,LTC,USDT&tsyms=USD,INR'
response = requests.get(url)
print(response.text)
rate = response.json()
print(type(rate))
for i in rate:
    print("-"*25)
    print(i + "-> USD:" + str(rate[i]["USD"]))
    print(i + "-> INR:" + str(rate[i]["INR"]) + "\n")


# # from requests import Request, Session
# # from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# # import json

# # url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# # parameters = {
# #   'start':'1',
# #   'limit':'5000',
# #   'convert':'INR'
# # }
# # headers = {
# #   'Accepts': 'application/json',
# #   'X-CMC_PRO_API_KEY': '',
# # }

# # session = Session()
# # session.headers.update(headers)

# # try:
# #   response = session.get(url, params=parameters)
# #   data = json.loads(response.text)
# #   print(data)
# # except (ConnectionError, Timeout, TooManyRedirects) as e:
# #   print(e)

# import re
# import sys
# import csv
# import time
# import random
# import requests
# from datetime import date
# from bs4 import BeautifulSoup

# end_date = str(date.today()).replace("-","")
# base_url = "https://coinmarketcap.com/currencies/{0}/historical-data/?start=20130428&end="+end_date

# currency_name_list = ["bitcoin", "ethereum", "ripple", "bitcoin-cash", "nem", "litecoin", "dash", "ethereum-classic", "iota", "neo", "stratis", "monero", "waves", "bitconnect", "omisego", "qtum", "numeraire"]


# def get_data(currency_name):
#     print("Currency : ", currency_name)
#     url = base_url.format(currency_name)
#     html_response = requests.get(url).text.encode('utf-8')
#     soup = BeautifulSoup(html_response, 'html.parser')
#     table = soup.find_all('table')[0]
#     elements = table.find_all("tr")
#     with open("./{0}_price.csv".format(currency_name.replace("-","_")),"w") as ofile:
#         writer = csv.writer(ofile)
#         for element in elements:
#             writer.writerow( element.get_text().strip().split("\n") )
#     time.sleep(1)

# if __name__ == "__main__":
#     for currency_name in currency_name_list:
#         get_data(currency_name)
#         pass


