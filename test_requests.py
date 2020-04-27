import json
import requests
from requests import Response
from jsonpath import jsonpath
from jsonschema import validate


class TestHttp:
    def test_get(self):
        r = requests.get('https://testerhome.com/hogwarts')
        print(r)

    def test_get_query(self):
        url = "http://47.95.238.18:8090/#/HTTP_Methods/get_get"
        params = {'wd':'mp3', 'fenlei':['2', '3']}
        r = requests.get(url, params=params)
        self.inspect_r_response(r)

    def test_get_query_header(self):
        url = "http://47.95.238.18:8090/get"
        params = {'wd': 'mp3', 'fenlei': ['2', '3']}
        headers = {'a': 'a1', 'b': 'b1', 'accept': "application/json"}
        r = requests.get(url, params=params, headers=headers)
        self.inspect_r_response(r)

    def test_post(self):
        url = "http://47.95.238.18:8090/post"
        data = {'wd': 'mp3', 'fenlei': ['2', '3']}
        jsons = {'wd': 'mp4', 'fenlei': ['2', '3']}
        headers = {'a': 'a1', 'b': 'b1', 'accept': "application/json"}
        proxies = {'http': '127.0.0.1:8888'}
        r = requests.post(url, data=data, json=jsons, headers=headers, proxies=proxies)
        self.inspect_r_response(r)

    def inspect_r_response(self, r: Response):
        print(r)
        print(r.text)
        print(r.content)
        print(r.url)
        print(r.cookies)
        print(r.headers)
        print(r.status_code)
        print(r.encoding)
        print(r.raw)
        # print(r.json())

    def test_testerhome_get(self):
        url = 'http://testerhome.com/api/v3/topics.json'
        params = {'limit': 2}
        r = requests.get(url, params=params)
        print(r.json())
        # assert r.json()['topics'][0]['id']==23339
        assert r.json()['topics'][-1]['user']['login'] == 'simple'

    def test_testerhome_get_jsonpath(self):
        url = 'http://testerhome.com/api/v3/topics.json'
        params = {'limit': 2}
        data = requests.get(url, params=params).json()

        print(jsonpath(data, '$..user'))

        list_id = jsonpath(data, "$.topics[?(@.user.login == 'stu.yu')].id")
        assert list_id[0] == 23352

    '''
    def test_testerhome_get_hamcrest(self):
        assert_that(0.1*0.1, close_to(0.01, 0.0001))
        assert_that(
            ["a", "b", "c"],
            all_of(
                has_items("c", "d"
                               ""),
                has_items("c", "a")
            )
        )
    '''

    def test_testerhome_get_schema(self):
        url = 'http://testerhome.com/api/v3/topics.json'
        params = {'limit': 2}
        data = requests.get(url, params=params).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)

    def test_xueqiu_get(self):
        url = 'https://xueqiu.com/stock/search.json'
        params = {'code':'sogo', 'size':3, 'page': 1}
        header = {'Accept': "application/json",
                  'User-Agent':
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
                  }
        cookies = {"xq_a_token": "48575b79f8efa6d34166cc7bdc5abb09fd83ce63"}
        data = requests.get(url, params=params, headers=header, cookies=cookies).json()
        assert data['stocks'][0]['name'] == "搜狗"

