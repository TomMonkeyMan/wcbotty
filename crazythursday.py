# python3
# 没有做异常判断，建议自行做http状态的判断，以及.json()获取
import requests
def get_crazythursday():
    url = "https://api.shadiao.pro/kfc"
    res = requests.get(url)
    return(res.json()['data']['text'])
