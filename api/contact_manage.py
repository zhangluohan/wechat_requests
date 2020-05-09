import requests

from api.base_api import BaseApi
from api.work import Work
from utils.util import Util


class ContactManage(BaseApi):

    _url_create = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    _url_list = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
    _url_delete = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
    _url_update = "https://qyapi.weixin.qq.com/cgi-bin/user/update"

    def create_contact(self, userid, name, alias, mobile, department):
        data = {"userid": userid, "name": name, "alias": alias, "mobile": mobile, "department": department}
        self.json_object = requests.post(self._url_create,
                          params={"access_token": Work().get_token_contact()},
                          json=data,
                          headers={'content-type': 'application/json; charset=utf-8'}
                          ).json()
        self.base_json_format(self.json_object)
        return self.json_object

    def list_contact(self, userid):
        r = requests.get(self._url_list,
                         headers={'content-type': 'application/json; charset=utf-8'},
                         params={"access_token": Work().get_token_contact(), "userid": userid}).json()
        return r

    def update_contact(self, userid, name):
        data = {"userid": userid, "name": name}
        r = requests.post(self._url_update,
                          params={"access_token": Work().get_token_contact()},
                          json=data
                          ).json()
        self.base_json_format(r)
        return r

    def delete_contact(self, userid):
        r = requests.get(self._url_delete,
                         params={"access_token": Work().get_token_contact(), "userid": userid}).json()
        return r
