import itchat
import time
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import threading


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    if "I'm you father" in msg:
        print("I got a msg", msg.text)
        return "You piece of shit"


def after_login():
    print("I'm logging in")


def after_logout():
    print("I'm logging out")


def notify_lose_weight(itchat):
    quote_list = []
    with open("./static/sadhguru.quote") as file:
        for i in file.readlines():
            quote_list.append(i)
    boom_remark_name = ["DT_Molly", "Tianyu"]
    for each_friend in boom_remark_name:
        friends_info = itchat.search_friends(name=each_friend)
        print(friends_info)
        for i in range(2):
            rand_num = np.random.random_integers(len(quote_list) - 1)
            quote_to_friends = quote_list[rand_num]


def start_scheduler():
    # Create an instance of the scheduler
    scheduler = BackgroundScheduler()

    # Add a job to be executed at 9am, 12pm, and 6pm
    scheduler.add_job(notify_lose_weight, "cron", hour="9,12,18")

    # Start the scheduler
    scheduler.start()

    try:
        # Keep the main thread running to prevent the program from exiting
        while True:
            pass
    except KeyboardInterrupt:
        # Stop the scheduler if interrupted
        scheduler.shutdown()


if __name__ == "__main__":
    itchat.auto_login(
        hotReload=True,
        loginCallback=after_login,
        exitCallback=after_logout,
        enableCmdQR=2,
    )

    # Start the scheduler in a new thread
    scheduler_thread = threading.Thread(target=start_scheduler)
    scheduler_thread.start()

    itchat.run()
    itchat.logout()
    scheduler_thread.join()
