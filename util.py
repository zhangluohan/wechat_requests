import json

from jsonpath import jsonpath


class Util:

    def json_format(self, json_object):
        return json.dumps(json_object, indent=2)

    def jsonpath(self, json_object, json_find):
        return jsonpath(json_object, json_find)