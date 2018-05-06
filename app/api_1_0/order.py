from app import util
from app.model.food import *
from app.model.order_item import *
from . import api
import json
from flask import request

__route__ = '/order'

"""
添加
"""


@api.route(__route__, methods=['POST'])
def order_add():
    result = {"code": 10000, "value": "", "msg": "添加成功"}
    data = request.data
    data_dict = json.loads(data)

    print(data_dict)

    print(data_dict['foods'])

    for food in data_dict['foods']:
        print(food['sha_id'])
        print(food['num'])

        dic_food = Food.get_food(food['sha_id'])[0]

        # order_item = {}
        #
        # order_item['item_sha_id'] = ''
        # order_item['title'] = ''

        print(dic_food)

        orderItem = OrderItem()

        orderItem.num = food['num']
        orderItem.price = dic_food['price']
        orderItem.title = dic_food['title']


        orderItem.descript()



    return result
