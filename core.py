import threading
import logging
import time

from lib import helpers, client, config, private
from model import mail_bot

# log = logging.getLogger()
# log.setLevel(logging.info)


def main():
    maxtool = client.Client(private.key, private.secret)

    models = [mail_bot.mail_bot('ethtwd', 56000),
              mail_bot.mail_bot('maxtwd', 18.1)]

    while(True):
        for m in models:
            mail_list = m.get_mail(maxtool)
            for mail in mail_list:
                for t in config.EMAIL:
                    print(f"send email to {t}!!")
                    helpers.send_mail(t, mail)

            # buyList = m.getBuy(maxtool)
            # for buy in buyList:
            #     maxTool.buy(buy)

            # sellList = m.getSell(maxtool)
            # for sell in sellList:
            #     maxTool.sell(sell)

            m.count_down(config.SLEEP)
        time.sleep(config.SLEEP)


if __name__ == "__main__":
    main()
