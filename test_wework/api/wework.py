import requests

from test_wework.api.BaseApi import BaseApi


class WeWork(BaseApi):

    # corpid = "ww564d8f5d009b85a4"
    corpid = "ww93348658d7c66ef4"
    agent_id ="1000002"
    agent_secret = "ZA9Gngw9dBQ7uM_0sQP_6FQFkPXzMstnIjnrBrDUJ-E"
    # contact_secret = "qD6F5u-0SoHMxR8-gNDbqd9208ige4GwaWngm2dg7cU"
    contact_secret = "T0TFrXmGYel167lnkzEydsjl6bcDDeXVmkUnEYugKIw"
    access_token = None
    @classmethod
    def get_token(cls):
        if cls.access_token == None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r = requests.get(url,params={"corpid":cls.corpid,"corpsecret":cls.contact_secret}).json()
            print("first_get_token")
            cls.verbose(r)
            print(r)
            # 类变量
            cls.access_token = r["access_token"]

        return WeWork.access_token