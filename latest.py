import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from prettytable import PrettyTable
import json
import datetime
from datetime import date
from datetime import datetime, timedelta
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=date_added' 
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}

###########################################################################################################################                                                                                                                          #
headers = {                                                                                                               #
  'content-type': 'application/json',                                                                                     #
  'X-CMC_PRO_API_KEY': 'key', # sing up on https://pro.coinmarketcap.com/ and get your api key and paste instead word key #
}                                                                                                                         #
                                                                                                                          #
###########################################################################################################################



session = Session()
session.headers.update(headers)
def start():
  try: 
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    today = date.today()
    print(today)
    for entry in data["data"]:
      lastsymbol = entry["symbol"]
      name = entry["name"]
      lastdate_added_str = entry["date_added"][:10]
      print(name +" | "+ lastsymbol + ": " + lastdate_added_str)
      symbol = lastsymbol
      while symbol == lastsymbol:
        
        try: 
          response1 = session.get(url, params=parameters)
          data1 = json.loads(response1.text)

          for entry1 in data1["data"]:
            symbol = entry1["symbol"]
            name1 = entry1["name"]
            date_added_str = entry1["date_added"][:10]
            namer = name1.replace(' ', '-')
            print(namer)
            time.sleep(60)
        except(ConnectionError, Timeout, TooManyRedirects) as e:
          print(e)

      URL = 'https://coinmarketcap.com/currencies/' + namer 
      HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
      response = requests.get(URL, headers = HEADERS)
      soupe = BeautifulSoup(response.content, 'html.parser')
      items = str(soupe.find("span", class_ = 'mainChainTitle'))
      if "BEP20" in items:
          print('BSC')
          now = datetime.now()
          current_time = now.strftime("%H:%M:%S")
          print(namer +" | "+symbol + ": " + date_added_str + " | " + current_time)
          
          
          os.system("start https://coinmarketcap.com/currencies/" + namer)
          items1 = soupe.find("div", class_="sc-10up5z1-5 jlEjUY")
          items11 = str(items1.find("a", target="_blank", class_="cmc-link").get("href"))
          print(items11)
          abc = items11.split("/")
          print(abc[-1])
          os.system("start https://poocoin.app/tokens/" + abc[-1])
          os.system("start https://www.youtube.com/watch?v=gwgaxaRrtbk")
          start()
      else:
        start()
  except(ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


start()






