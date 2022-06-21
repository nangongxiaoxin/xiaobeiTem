# !/usr/bin/env python
# coding=utf-8
import requests, time, re, json,random

#Server酱推送提醒，需要填写sckey，官网：https://sc.ftqq.com/3.version
SCKEY = "***************************"

#SERVER酱微信推送url
scurl = f"https://sc.ftqq.com/{SCKEY}.send"

url="https://xiaobei.yinghuaonline.com/xiaobei-api/student/health"

def main_handler(userAgent,authorization):
    ran_1=str(random.randint(27,57))
    ran_2=str(random.randint(42,92))
    ran_time=random.randint(1,10)
    
    # 延迟
    print("延迟"+str(ran_time)+"执行")
    time.sleep(ran_time)


    headers = {
        "User-Agent": "Mozilla/5.0 M************",
        "Authorization": "Bearer ey*************",
        # "User-Agent":userAgent,
        # "Authorization":authorization,

        "Referer": url,
        "Content-Type": "application/json",
        "Content-Length": "260",
        "Host": "xiaobei.yinghuaonline.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        }
    data = {
        "temperature": "36",
        "coordinates": "中国-陕西省-西安市-高陵区",
        "location": "109.1142"+ran_1+",34.5364"+ran_2,
        "healthState": "1",
        "dangerousRegion": "2",
        "dangerousRegionRemark": "",
        "contactSituation": "2",
        "goOut": "1",
        "goOutRemark": "",
        "remark": "",
        "familySituation": "1"
    }
    data = json.dumps(data)
    r = requests.post(url, data=data, headers=headers, timeout=5)
    print(r.text)
    msg=r.json()["msg"]

    pushWechat(msg)

    return msg
    
# 微信推送
def pushWechat(msg):

    if "成功" in msg:
        params = {
            "text": "小北打卡成功",
            "desp": msg
        }
    else:
        params = {
            "text": "小北打卡失败",
            "desp": msg
        }
    requests.post(scurl,params=params)


