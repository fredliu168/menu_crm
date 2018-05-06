# -*- coding: utf-8 -*-
# 菜品
# 20180426

import json
from .. import dbManager

class Food(object):

    def __init__(self):
        self.id = 0
        self.sha_id = ''
        self.title = ''
        self.post_time = ''
        self.modify_time = 0
        self.price = 0
        self.discount_price = 0
        self.unit = 0
        self.total_num = 0
        self.description = 0

    @staticmethod
    def get_food(sha_id):
        sql = """select * from foods t where t.sha_id='{sha_id}'""".format(sha_id=sha_id)

        food = dbManager.exec_sql(sql)

        return food


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
