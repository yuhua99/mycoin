import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import time as _time

from lib.private import email_sender, email_pwd


def get_current_timestamp():
    return int(round(_time() * 1000))


def sleepTime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


def get_truncated_value(value, decimal=8):
    _int, _float = f"{float(value):.8f}".split('.')
    truncated = f"{int(_int)}.{_float[0:decimal]}"

    return float(f"{float(truncated):.{decimal}f}") if decimal > 0 else int(f"{float(truncated):.{decimal}f}")


def send_mail(recv, mail_info):
    if not mail_info:
        return
    
    mail = MIMEMultipart()
    mail["subject"] = mail_info[0]
    mail["from"] = email_sender
    mail["to"] = recv
    mail.attach(MIMEText(mail_info[1]))
    # set smtp server
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(email_sender, email_pwd)  # 登入寄件者gmail
            smtp.send_message(mail)  # 寄送郵件
            # print("Email sended!")
        except Exception as e:
            print("Error message: ", e)

    # for debug
    
    # print("___________email content____________")
    # print(mail_info[0])
    # print()
    # print(mail_info[1])
    # print("____________________________________")