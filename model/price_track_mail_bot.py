from lib.config import *
from lib.helpers import *
from model.model import Model


class pt_mail_bot(Model):
    def __init__(self, mt, pair='ethtwd', info={'percent': [[], []]}, base_price=-1):
        self.pair = pair
        self.base_price = base_price
        self.info = info
        # info['percent'][0] is down percentage
        # info['percent'][1] is up percentage

        # set default timer cool down to 10 min
        if 'cd' not in info:
            info['cd'] = [[], []]
            for i in range(2):
                info['cd'][i] = [sleepTime(0, 10, 0)] * len(info['percent'][i])

        self.timer = [[0] * len(info['cd'][0]),
                      [0] * len(info['cd'][1])]

        # set default base_price to current price
        if self.base_price == -1:
            self.base_price = float(
                mt.get_public_all_tickers(self.pair)['last'])

    def get_mail(self, mt):
        mail_list = [[], []]

        cur_price = float(mt.get_public_all_tickers(self.pair)['last'])

        for i in range(len(self.info['percent'][0])):
            pct = self.info['percent'][0][i]
            if cur_price <= self.base_price * (1 - 0.01 * pct):
                if self.timer[0][i] <= 0:
                    mail_list[0] = [
                        f"{self.pair} price is {pct}% lower than base price!",
                        f"Current price = {cur_price}\n"
                        + f"Base price = {self.base_price}\n"
                    ]
                    self.timer[0][i] = self.info['cd'][0][i]

        for i in range(len(self.info['percent'][1])):
            pct = self.info['percent'][1][i]
            if cur_price >= self.base_price * (1 + 0.01 * pct):
                if self.timer[1][i] <= 0:
                    mail_list[1] = [
                        f"{self.pair} price is {pct}% higher than base price!",
                        f"Current price = {cur_price}\n"
                        + f"Base price = {self.base_price}\n"
                    ]
                    self.timer[1][i] = self.info['cd'][1][i]

        return mail_list

    def count_down(self, cd_v):
        for i in range(2):
            for j in range(len(self.timer[i])):
                if self.timer[i][j] != 0:
                    self.timer[i][j] -= cd_v
        # print(self.timer)
