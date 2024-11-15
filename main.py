import itchat
import time
import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import threading
from crazythursday import get_crazythursday
from cheesylines import get_cheesylines

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    
    #print("I got a msg", msg.text)
    if "地震高岗" == msg.text.strip():
        return "一派西山千古秀"
    if "门朝大海" == msg.text.strip():
        return "三河合水万年流"
    if "地震高岗" in msg.text.strip():
        if "一派西山千古秀" in msg.text.strip():
            if ("门朝大海") not in msg.text.strip():
                if "三河合水万年流" not in msg.text.strip():
                    return "门朝大海, 三河合水万年流"
    if "请查询tianyu的日程" == msg.text.strip():
        #tianyu_shcedule = '''20240616 舌头X突突二重奏X李剑虹 上海万代南梦宫
#20240706 当代电影大师X伤心欲绝 上海万代南梦宫
#20240821 晨曦光廊 上海MAO'''
        tianyu_shcedule = ''''''
        return tianyu_shcedule
    if "给我疯狂星期四" == msg.text.strip():
        return get_crazythursday()
    
    user = msg['User']
    if user["RemarkName"] == "女朋友":
        if "爱我么" in msg.text.strip():
            return "爱你哦，啵啵"
        if "啵啵" in msg.text.strip():
            return "啵啵"
        if "土味情话" in msg.text.strip():
            return get_cheesylines()
    #print(user)get_cheesylines()

    
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def reply_msg_group(msg):
    #print("I got a msg", msg.text)
    if "给我疯狂星期四" == msg.text.strip():
        return get_crazythursday() 

#@itchat.msg_register([itchat.content.RECORDING, itchat.content.PICTURE])
#def download_files(msg):
#    msg.download(msg.fileName)   # 通过文件名下载文件

def after_login():
    print("I'm logging in")


def after_logout():
    print("I'm logging out, this is a note message. Keep learn leetcode...")


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
            itchat.send(f"[AWESOMEO-{i}]: " + quote_to_friends + "\npls lose some weight~", toUserName=friends_info[0]['UserName'])

def notify_cheesy_lines(itchat):
    chessy_line = get_cheesylines()
    user_name = itchat.search_friends(name=u'女朋友')[0]
    print("debug notify_cheesy_lines", user_name)
    #memberList = itchat.get_friends()[:10]
    #print("debug notify_cheesy_lines", memberList)
    
    itchat.send(chessy_line, toUserName=user_name['UserName'])

def start_scheduler():
    # Create an instance of the scheduler
    scheduler = BackgroundScheduler()

    # Add a job to be executed at 9am, 12pm, and 6pm
    #scheduler.add_job(lambda: notify_lose_weight(itchat), "cron", hour="9,12,18")
    scheduler.add_job(lambda: notify_cheesy_lines(itchat), "cron", hour="0,6,12,18")
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
