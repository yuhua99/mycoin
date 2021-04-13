from lib.config import *
from lib.helpers import *
from model.model import Model

class mail_bot(Model):
    def __init__(self):
        # timer for 7, 14, 30 low, 7, 14, 30 high, target price
        self.timer = [0, 0, 0, 0, 0, 0, 0]
    
    def get_buy(self, mt, pair = 'maxtwd'):
        
    def get_sell(self, mt, pair = 'maxtwd'):
    
    def count_down(self, cd_v):
        for i in range(len(self.timer)):
            if self.timer[i] != 0:
                self.timer[i] -= cd_v
        # print(self.timer)