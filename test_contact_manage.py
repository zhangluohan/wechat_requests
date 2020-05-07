from datetime import datetime

from service.test_wechat_requests_V1.api.contact_manage import ContactManage
from service.test_wechat_requests_V1.utils.util import Util


class TestContactManage:
    contact = ContactManage()

    def test_get_contact_list(self):
        assert self.contact.list_contact("zhangguangxing")["name"] == "张光兴"

    def test_create_contact(self):
        username = "user" + str(datetime.now().second)
        assert self.contact.create_contact(username, "王五125", "wangwu125", "13810001006", [1])["errmsg"] == "created"
        # TODO:调用list api,在验证是在列表中，用jsonpath

    def test_delete_contact(self):
        username = "user"+str(datetime.now().second)
        self.contact.create_contact(username, "xiaoxiao123", "xiaoxiao123", "13801000016", [1])
        assert self.contact.delete_contact(username)["errmsg"] == "deleted"

    def test_update_contact(self):
        assert self.contact.update_contact("useridlisi", "丽莎2")["errmsg"]=="updated"
