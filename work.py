import requests as requests


class Work:
    _url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'  # 此值对于大家来说固定，所以写在init里边,也可以写到 cfg中
    _corpid = 'ww26eb2bbc4cda1b4c'
    _secret_contact = "MJa-vSiW-gmn6_zZQ0rIR_83MFEOuytxWTd2YRm0s44"
    _secret_req_mine = "gznGUdBUK4hCPF8kT06Q88n9dZKDYhTzs7ybBoiq6xg"
    token_contact = None
    token_req_mine = None

    @classmethod
    def get_token_contact(cls):

        if cls.token_contact is None:
            send_json_contact = {"corpid": cls._corpid, "corpsecret": cls._secret_contact}
            cls.token_contact = requests.get(cls._url, params=send_json_contact).json().get('access_token')
            print("----1---token----" + cls.token_contact)

        return cls.token_contact

    @classmethod
    def get_token_req_mine(cls):

        if cls.token_req_mine is None:
            send_json_req_mine = {"corpid": cls._corpid, "corpsecret": cls._secret_req_mine}
            cls.token_req_mine = requests.get(cls._url, params=send_json_req_mine).json().get('access_token')
            print("----1---token----" + cls.token_req_mine)

        return cls.token_req_mine
