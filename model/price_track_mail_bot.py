from lib.config import *
from lib.helpers import *
from model.model import Model

class mail_bot(Model):
    def __init__(self, pair = 'ethtwd', base_price = -1, percent = {'up':[], 'down':[]}):
        # timer for 7,14,30 low, 7,14,30 high, target price
        self.pair = pair
        self.base_price = base_price
        self.percent = percent
        self.timer = {'up'  : [0] * len(PT_MAIL_BOT_CD['up']),
                      'down': [0] * len(PT_MAIL_BOT_CD['down'])}

        # default to current price
        if self.base_price = -1:
            self.base_price = float(mt.get_public_all_tickers(self.pair)['last'])
    
    def get_mail(self, mt):
        mail_list = []

        cur_price = float(mt.get_public_all_tickers(self.pair)['last'])

        for i in range(len(self.timer['up'])):
            if
        
        return mail_list
    
    def count_down(self, cd_v):
        for i in range(len(self.timer['up'])):
            if self.timer['up'][i] != 0:
                self.timer['up'][i] -= cd_v
        for i in range(len(self.timer['down'])):
            if self.timer['down'][i] != 0:
                self.timer['down'][i] -= cd_v
        # print(self.timer)