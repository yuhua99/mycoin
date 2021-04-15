在lib新增一個private.py
內容如下
``` py=
# MAX api key
key = 'YOUR KEY'
secret = 'YOUR SECRET'

# email account
email_sender = "YOUR GMAIL"
email_pwd = "YOUR PWD TEST"
```

## model usage

### mail bot
在`core.py`的`models`新增`mail_bot.mail_bot(PAIR, TARGET_PRICE)`

- PAIR : 交易對，像是'ethtwd'
- TARGET_PRICE : 目標價格，低於目標價格時會寄信通知

```py=
mail_bot.mail_bot('ethtwd', 55000)
```

### price track mail bot
在`core.py`的`models`新增`price_track_mail_bot.pt_mail_bot(maxtool, PAIR, INFO, BASE_PRICE)`

- PAIR : 交易對，像是'ethtwd'
- INFO : 資訊
    ```py=
    {
        'percent':[[a, b, c, ...], [x, y, z, ...]]
        'cd':[[A, B, C, ...], [X, Y, Z, ...]]
    }
    ```
    percent[0]是當前價格低於基準價格a%, b%, c%時會寄信通知， 要填幾個都可以
        percent[1]是當前價格高於基準價格...

        cd是對應的寄信間隔時間，如果不填預設是10分鐘

- BASE_PRICE : 基準價格，如果不填預設是當前價格

```py=
price_track_mail_bot.pt_mail_bot(maxtool, 'ethtwd', {'percent':[[1, 1,5], [0.5, 2]]})
price_track_mail_bot.pt_mail_bot(
    maxtool,
    'ethtwd',
    {
        'percent':[[1, 1,5], [0.5]],
        'cd':[
            [helpers.sleepTime(0, 15, 0), helpers.sleepTime(0, 5, 0)],
            [helpers.sleepTime(0, 15, 0)]
        ]
    }
)
```