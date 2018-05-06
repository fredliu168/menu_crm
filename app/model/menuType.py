# -*- coding: utf-8 -*-
# 菜单类型
# 20180426

import json

from .. import dbManager


class MenuType(object):

    def __init__(self):
        self.id = 0
        self.sha_id = ''
        self.title = ''
        self.image_id = ''
        self.type_index = 0
        self.modify_time = ''


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def descript(self):
        print(self.id)
        print(self.sha_id)
        print(self.title)
        print(self.image_id)
        print(self.type_index)
        print(self.modify_time)
