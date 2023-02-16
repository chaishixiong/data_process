import requests
import time
import hmac
import hashlib
import base64
import urllib.parse
import json

def dingding_prame(secret):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp,sign

def request_dingding(text):
    secret = 'SEC7e1315fffc86d24b72dba8ed8771bb3f2686d274a8247b80ddc9e5792a0283bf'
    access_token = "967938e4c7311b536c3f766f650358727e3ed3678bf71d7bce310555703527a7"
    timestamp,sign = dingding_prame(secret)
    url = "https://oapi.dingtalk.com/robot/send?access_token={}&timestamp={}&sign={}".format(access_token,timestamp,sign)
    data = {
        "msgtype": "text",
        "text": {
            "content": "{}".format(text)
        },
        "at": {
            "atMobiles": [
            ],
            "isAtAll": False
        }
    }
    req = requests.post(url,json=data)
    return req.text

def run(request_text):
    result_text = request_dingding(request_text)
    result = json.loads(result_text)
    if result.get("errcode") != 0:
        time.sleep(60)
        text = request_dingding(request_text)

if __name__=="__main__":
    new_table = 10
    loads_success_table = 10
    online_error_table = 0
    request_text = '''电商数据周备份:
    新增备份数量:{}
    下载成功数量:{}
    压缩错误数量:{}
    '''.format(new_table,loads_success_table,online_error_table)
    run(request_text)

