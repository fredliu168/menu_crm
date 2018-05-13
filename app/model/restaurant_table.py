# -*- coding: utf-8 -*-
import json
import os
import requests
from app import util
from .. import dbManager

class Table(object):
    def __int__(self):
        self.id = 0
        self.title = ''  # 名称
        self.number = 0  # 编号
        self.sha_id = ''

    def get(self,sha_id):
        sql = """select * from restaurant_tables t where t.sha_id='{sha_id}'""".format(sha_id=sha_id)

        print(sql)

        table_dic = dbManager.exec_sql(sql)

        print(table_dic)

        if len(table_dic) >0:

            return self.dict2obj(table_dic[0])
        else:
            return None


    def dict2obj(self, d):
        if isinstance(d, Table):
            d = [self.dict2obj(x) for x in d]
        if not isinstance(d, dict):
            return d
        for k in d:
            self.__dict__[k] = self.dict2obj(d[k])
        return self