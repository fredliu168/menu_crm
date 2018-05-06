# -*- coding: utf-8 -*-
# 订单详单
# 20180428

import json
from .. import dbManager
import datetime


class OrderItem(object):

    def __init__(self):
        self.item_sha_id = ''
        self.title = ''
        self.price = 0
        self.num = 0
        self.post_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save(self):
        pass

    def descript(self):
        print(self.post_time)
        print(self.title)
        print(self.price)
        print(self.num)
