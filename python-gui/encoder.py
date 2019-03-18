import json
from domain import Menu


class MenuEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Menu):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)

