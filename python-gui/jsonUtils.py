# -*- coding:utf-8 -*-

import json
from encoder import MenuEncoder


class JsonUtils(object):
    def __init__(self):
        super(JsonUtils, self).__init__()

    @staticmethod
    def obj_2_json(obj):
        json_data = json.dumps(obj, cls=MenuEncoder)
        return json_data


def main():
    print()


if __name__ == '__main__':
    main()
