import pytest

from service.test_wechat_requests_V1.api.message_manage import MessageManage


class TestMessageManage:
    message = MessageManage()

    @pytest.mark.parametrize("text",["你的","nide", "dfsdfsdf","eferter"])
    def test_send_text(self,text):
        # text = "你的快递。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
        assert self.message.send_text("WangPei", text)["errmsg"] == "ok"

    def test_send_image(self):
        image = "37OD-adY8kVpml03tGihL5ITShjAM1kE4cnrQ7kiEVxk"
        assert self.message.send_image("WangPei", image)["errmsg"] == "ok"
