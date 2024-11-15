import requests

def get_cheesylines():
    url = "https://api.shadiao.pro/chp"
    res = requests.get(url)
    if res.status_code == 200:
        return(res.json()['data']['text'])
#def get_cheesylines2():
    url = "https://api.lovelive.tools/api/SweetNothings"
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
