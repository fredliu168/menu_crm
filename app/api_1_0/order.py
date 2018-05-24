from app import util
from app.model.food import *
from app.model.user import *
from app.model.order_item import *
from app.model.restaurant_table import *
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
    data_dict = json.loads(data.decode('utf-8'))

    print(data_dict)

    print(data_dict['foods'])

    user = User()
    user_obj = user.get_user(data_dict['user_sha_id'])
    print(user_obj.phoneNumber)

    table = Table()

    table_obj = table.get(data_dict['table_sha_id'])

    if table_obj == None:
        result['code'] = -10000
        result['msg'] = '桌号错误，找不到对应餐桌！'
        return result

    print(table_obj.title)

    sql_list = []
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

        if food['num'] > dic_food['total_num']:
            result['code'] = -10000
            result['msg'] = '{title}数量超过库存{num}{unit}，请修改订单'.format(title=dic_food['title'], num=dic_food['total_num'],
                                                                    unit=dic_food['unit'])
            return result

        # dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(dt)
        orderItem.num = food['num']
        orderItem.price = dic_food['price']
        orderItem.title = dic_food['title']
        orderItem.food_sha_id = food['sha_id']
        orderItem.item_sha_id = util.MD5(
            orderItem.post_time + str(orderItem.num) + str(orderItem.price) + orderItem.title + orderItem.food_sha_id)
        orderItem.descript()

        sql = 'update foods set total_num =total_num-{num} where sha_id={sha_id}'.format(num=orderItem.num,
                                                                                         sha_id=orderItem.food_sha_id)
        sql_list.append(sql)

        sql_items = '''insert into order_items(item_sha_id,food_sha_id,title,price,post_time,num)
 values ('{item_sha_id}','{food_sha_id}','{title}',{price},'{post_time}',{num})'''.format(
            item_sha_id=orderItem.item_sha_id,
            food_sha_id=orderItem.food_sha_id,
            title=orderItem.title,
            price=orderItem.price,
            post_time=orderItem.post_time,
            num=orderItem.num)

        print(sql_items)
        sql_list.append(sql_items)

        sql_oder_items = '''insert into foods_order_items(order_sha_id,item_sha_id) values ('{order_sha_id}','{item_sha_id}')'''.format(
            order_sha_id='', item_sha_id='')

    return result
