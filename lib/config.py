from lib.helpers import *

# --------------------------PARAMETERS------------------------
SLEEP = sleepTime(0, 0, 15)  # 每隔幾秒重新抓一次
# EMAIL = ["fishtoby.cs06@nctu.edu.tw", "Annie@ttime.com.Tw"]
EMAIL = ["larry99.yh@gmail.com"]
# 抓最低價的url
PREFIX = "https://www.coingecko.com/price_charts/279/twd/"

MAIL_BOT_CD = [
    sleepTime(0, 10, 0),         # 7天內最低價格寄信間隔
    sleepTime(0, 10, 0),         # 14天內最低價格寄信間隔
    sleepTime(0, 10, 0),         # 30天內最低價格寄信間隔
    sleepTime(0, 10, 0),         # 7天內最高價格寄信間隔
    sleepTime(0, 10, 0),         # 14天內最高價格寄信間隔
    sleepTime(0, 10, 0),         # 30天內最高價格寄信間隔
    sleepTime(0, 10, 0)          # 目標價格寄信間隔
]

# ------------------------------------------------------------

# --------------------------CONSTANTS-------------------------
PUBLIC_API_URL = 'https://max-api.maicoin.com/api'
PRIVATE_API_URL = 'https://max-api.maicoin.com/api'

PUBLIC_API_VERSION = 'v2'
PRIVATE_API_VERSION = 'v2'
# ------------------------------------------------------------
