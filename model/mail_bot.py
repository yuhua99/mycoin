from lib.config import *
from lib.helpers import *
from model.model import Model

class mail_bot(Model):
    def __init__(self, pair = 'ethtwd', target_price = 999999):
        # timer for 7, 14, 30 low, 7, 14, 30 high, target price
        self.timer = [0, 0, 0, 0, 0, 0, 0]
        self.pair = pair
        self.target_price = target_price
    
    def get_mail(self, mt):
        tmp = ['7', '14', '30']
        mail_list = []

        cur_price = float(mt.get_public_all_tickers(self.pair)['last'])
        k_line = mt.get_public_k_line(self.pair, 4, 60*24*7)     # 拿4個週期為7天的k line
        history_price = [k_line[0][3],                                                 # 7天最低
                         min(k_line[0][3], k_line[1][3]),                              # 14天最低
                         min(k_line[0][3], k_line[1][3], k_line[2][3], k_line[3][3]),  # 30天最低
                         k_line[0][2],                                                 # 7天最高
                         max(k_line[0][2], k_line[1][2]),                              # 14天最高
                         max(k_line[0][2], k_line[1][2], k_line[2][2], k_line[3][2])]  # 30天最高

        # low price mail generate
        for i in range(2, -1, -1):
            if cur_price <= history_price[i]:
                if self.timer[i] <= 0:
                    mail_list.append(
                        [(f"{self.pair} lowest price in last {tmp[i]} days!"),
                         (f"Current price           = {cur_price}\n"
                        + f"Lowest price in 7  days = {history_price[0]}\n"
                        + f"Lowest price in 14 days = {history_price[1]}\n"
                        + f"Lowest price in 30 days = {history_price[2]}")]
                    )
                    self.timer[i] = MAIL_BOT_CD[i]
                    break
        # high price mail generate
        for i in range(5, -1, 2):
            if cur_price >= history_price[i]:
                if self.timer[i] <= 0:
                    mail_list.append(
                        [(f"{self.pair} highest price in last {tmp[i]} days!"),
                         (f"Current price           = {cur_price}\n"
                        + f"highest price in 7  days = {history_price[0]}\n"
                        + f"highest price in 14 days = {history_price[1]}\n"
                        + f"highest price in 30 days = {history_price[2]}")]
                    )
                    self.timer[i] = MAIL_BOT_CD[i]
                    break
        
        if cur_price <= self.target_price:
            if self.timer[-1] <= 0:
                mail_list.append(
                    [(f"{self.pair} lower than your target price {self.target_price}!"),
                     (f"Current price           = {cur_price}\n"
                    + f"Lowest price in 7  days = {history_price[0]}\n"
                    + f"Lowest price in 14 days = {history_price[1]}\n"
                    + f"Lowest price in 30 days = {history_price[2]}")]
                )
                self.timer[-1] = MAIL_BOT_CD[-1]
        return mail_list
    
    def count_down(self, cd_v):
        for i in range(len(self.timer)):
            if self.timer[i] != 0:
                self.timer[i] -= cd_v
        # print(self.timer)