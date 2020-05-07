import requests

from service.test_wechat_requests_V1.utils.util import Util


class BaseApi:
    json_object = None

    @classmethod
    def base_json_format(cls, json_object):
        print(Util().json_format(json_object))

    @classmethod
    def base_jsonpath(cls, json_find):
        return Util().jsonpath(cls.json_object, json_find)

    def base_request(self, method, url, params, json, proxies=""):
        requests.request(method, url=url, params=params, json=json, proxies=proxies, verity=False)
