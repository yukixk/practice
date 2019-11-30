import requests

from test_wework.api.BaseApi import BaseApi
from test_wework.api.wework import WeWork
from test_wework.utils.utils import Utils


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

    def list(self,id):
        r = requests.get(self.list_url,params={"access_token":WeWork.get_token(),"id":id}).json()
        self.verbose(r)
        return r
    def creat(self,name,parentid,order):
        data = {
            "name":name,
            "parentid":parentid,
            "order":order,
            "id":None
        }
        r = requests.post(self.create_url,json=data,params={"access_token":WeWork.get_token()}).json()
        self.verbose(r)
        return r
    def delete(self,id):
        r = requests.get(self.delete_url,params={"access_token":WeWork.get_token(),"id":id}).json()
        self.verbose(r)
        return r
    def update(self):
        pass