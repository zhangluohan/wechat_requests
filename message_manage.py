import requests

from service.test_wechat_requests_V1.api.base_api import BaseApi
from service.test_wechat_requests_V1.api.work import Work


class MessageManage(BaseApi):
    _url_send_message = "https://qyapi.weixin.qq.com/cgi-bin/message/send"

    def send_text(self, user, text):
        data = {"touser": user,
                "msgtype": "text",
                "agentid": 1000002,
                "text": {"content": text}
                }

        self.json_object = requests.post(self._url_send_message, params={"access_token": Work().get_token_req_mine()},
                                         json=data).json()
        return self.json_object

    def send_image(self, user, image):
        data = {
            "touser": user,
            "msgtype": "image",
            "agentid": 1000002,
            "image": {
                "media_id": image
            }
        }

        self.json_object = requests.post(self._url_send_message, params={"access_token": Work().get_token_req_mine()},
                                         json=data).json()
        return self.json_object
