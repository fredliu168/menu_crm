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

    def delete(self, sha_id):
        condition = {'sha_id': sha_id}
        dbManager.delete('menu_type', condition)

    def get(self, sha_id):
        sql = """select * from menu_type t where t.sha_id='{sha_id}'""".format(sha_id=sha_id)

        menu_type = dbManager.exec_sql(sql)

        if len(menu_type) == 1:
            return self.dict2obj(menu_type[0])
        else:
            return None


    def dict2obj(self, d):
        if isinstance(d, MenuType):
            d = [self.dict2obj(x) for x in d]
        if not isinstance(d, dict):
            return d
        for k in d:
            self.__dict__[k] = self.dict2obj(d[k])
        return self

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
