import itchat
import time
import numpy as np

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print("I got a msg", msg.text)

def after_login():
    print("I'm logging in")

def after_logout():
    print("I'm logging out")

if __name__ == "__main__":
    itchat.auto_login(
        hotReload=True,
        loginCallback=after_login, 
        exitCallback=after_logout, 
        enableCmdQR=2,
    )
    #time.sleep(2)
    quote_list = []
    with open("./static/sadhguru.quote") as file:
        for i in file.readlines():
            quote_list.append(i)
    boom_remark_name = ["DT_Molly", "Tianyu"]
    for each_friend in boom_remark_name:
        friends_info = itchat.search_friends(name = each_friend)
        print(friends_info)
        for i in range(2):
            rand_num = np.random.random_integers(len(quote_list)-1)
            quote_to_friends = quote_list[rand_num] 
            itchat.send(f"[AWESOMEO-{i}]: " + quote_to_friends + "\npls lose some weight~", toUserName=friends_info[0]['UserName'])
        #itchat.send(f"Hi this is Kenny-{i}, u need to lose some weight! Fatty!", toUserName=friends_info[0]['UserName'])
        #itchat.send(f"Hi this is Kenny-{i}, u need to lose some weight! Fatty!", toUserName=friends_info[0]['UserName'])
    #itchat.run()
    #time.sleep(2)
    #itchat.logout()
