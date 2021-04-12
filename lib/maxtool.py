import requests

from lib import helpers, config, client, private


class Maxtool():
    def __init__(self):
        self.api = client.Client(private.key, private.secret)
        self.cur_price = None
        
        # lowest price in 7, 14, 30 days
        self.histroy_price = [0.0, 0.0, 0.0]
        self.mail_queue = []
        # get price information
        self.get_history_price()
        self.get_cur_price()
    
    def get_cur_price(self, pair = 'ethtwd'):
        cur_price = api.get_public_all_tickers(pair)['last']
        

    def get_history_low_price(self):
        day7 = requests.get(PREFIX + "7_days.json").json()
        day14 = requests.get(PREFIX + "14_days.json").json()
        day30 = requests.get(PREFIX + "30_days.json").json()
        
        def get_low(data):
            tmp = 99999999.0
            for info in data['stats']:
                tmp = min(float(info[1]), tmp)
            return tmp
        
        self.low_price[0] = get_low(day7)
        self.low_price[1] = get_low(day14)
        self.low_price[2] = get_low(day30)

    def get_price_info(self):
        return (f"Current price           = {self.cur_price}\n"
              + f"Lowest price in 7  days = {self.low_price[0]}\n"
              + f"Lowest price in 14 days = {self.low_price[1]}\n"
              + f"Lowest price in 30 days = {self.low_price[2]}")
