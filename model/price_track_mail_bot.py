from lib.config import *
from lib.helpers import *
from model.model import Model


class mail_bot(Model):
    def __init__(self, mt, pair='ethtwd', base_price=-1, info={'percent': [[], []], 'cd': [[], []]}):
        # timer for 7,14,30 low, 7,14,30 high, target price
        self.pair = pair
        self.base_price = base_price
        self.info = info
        # info['percent'][0] is down percentage
        # info['percent'][1] is up percentage

        # set default timer cool down to 10 min
        for i in range(2):
            if not info['cd'][i]:  # if list is empty
                info['cd'][i] = [sleepTime(0, 10, 0)] * len(info['percent'][i])

        self.timer = [[0] * len(info['cd'][0]),
                      [0] * len(info['cd'][1])]

        # set default base_price to current price
        if self.base_price == -1:
            self.base_price = float(
                mt.get_public_all_tickers(self.pair)['last'])

    def get_mail(self, mt):
        mail_list = []

        cur_price = float(mt.get_public_all_tickers(self.pair)['last'])

        for pct in self.info['percent'][0]:
            if cur_price <= self.base_price * (1 + 0.01*pct):

        return mail_list

    def count_down(self, cd_v):
        for i in range(len(self.timer['up'])):
            if self.timer['up'][i] != 0:
                self.timer['up'][i] -= cd_v
        # print(self.timer)
