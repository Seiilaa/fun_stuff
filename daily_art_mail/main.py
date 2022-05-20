import schedule
import time
from html_template import html
from email_sender import send_email
import pickle

with open("art_dict.txt", "rb") as tf:
    art_dict = pickle.load(tf)

# the dict that contains names and emails of the users
receivers = {'Test': 'my.gmail.com'}

day = -1


def send_daily_email():
    global day
    day += 1
    print('The email №{} was sent!'.format(day))
    send_email(n=day, data_dict=art_dict, html=html, receivers=receivers)


# Task scheduling
# Every day at 10am send_daily_email is called.
schedule.every().day.at("10:00").do(send_daily_email)

# Loop so that the scheduling task
# keeps on running all time.
while day < 30:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
else:
    day = -1
    schedule.run_pending()
    time.sleep(1)
