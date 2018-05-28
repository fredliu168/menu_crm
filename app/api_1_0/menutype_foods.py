from app import util
from app.model.menuType import *
from . import api
import json
from flask import request
from collections import defaultdict

__table__ = "menutype_foods"  # 操作的表

"""
菜单分类对应的菜品
"""


@api.route("/food-type", methods=['GET'])
def get_menutype_foods():
    result = {"code": 10000, "value": "", "msg": ""}
    sql = """select mf.menu_sha_id,m.title as menu_title,mf.foods_sha_id,f.title as food_title,f.price,total_num,f.unit  from menutype_foods mf left join `menu_type` m on mf.`menu_sha_id` = m.sha_id 
left join `foods` f on mf.`foods_sha_id`=f.sha_id order by m.`type_index` desc,mf.`index` desc"""

    menu_types_foods = dbManager.exec_sql(sql)

    # 对返还的列表数据进行整理
    foods_dict = {}
    for menu_type_food in menu_types_foods:
        dict = {}
        for (k, v) in menu_type_food.items():
            if k != 'menu_title' and k != 'menu_sha_id':
                dict[k] = v

        if menu_type_food['menu_sha_id'] not in foods_dict.keys():
            # 如果不存在就新增
            foods_dict[menu_type_food['menu_sha_id']] = {"menu_sha_id": menu_type_food["menu_sha_id"],
                                                         "menu_title": menu_type_food["menu_title"], "foods": []}

        foods_dict[menu_type_food['menu_sha_id']]["foods"].append(dict)

    # 把字典进行处理,返还array数据
    foods_list = []
    for (k, v) in foods_dict.items():
        foods_list.append(v)

    result["value"] = foods_list
    result["msg"] = "获取数据成功"

    return result


@api.route("/food-type/<menu_sha_id>", methods=['GET'])
def get_menutype_foods_sha_id(menu_sha_id):
    result = {"code": 10000, "value": "", "msg": ""}
    sql = """select mf.sha_id as m_sha_id,f.*,1 as flag  from menutype_foods mf left join `menu_type` m on mf.`menu_sha_id` = m.sha_id 
left join `foods` f on mf.`foods_sha_id`=f.sha_id where m.sha_id = '{menu_sha_id} ' order by f.states desc, mf.`index` """.format(
        menu_sha_id=menu_sha_id)

    menu_types_foods = dbManager.exec_sql(sql)

    result["value"] = menu_types_foods
    result["msg"] = "获取数据成功"

    return result


@api.route("/food-type/un/<menu_sha_id>", methods=['GET'])
def get_unMenuType_foods_sha_id(menu_sha_id):
    """
    获取非该分类的物品
    :param menu_sha_id:
    :return:
    """
    result = {"code": 10000, "value": "", "msg": ""}
    sql = """select f.*,0 as flag  from foods  f where f.sha_id not in (select mf.`foods_sha_id` from `menutype_foods` mf where mf.`menu_sha_id`='{menu_sha_id}')  order by f.food_index""".format(
        menu_sha_id=menu_sha_id)

    print(sql)
    menu_types_foods = dbManager.exec_sql(sql)

    result["value"] = menu_types_foods
    result["msg"] = "获取数据成功"

    return result


"""
添加
{
 "menu_sha_id":"22f0b4efe54e3d6e6dcc719c79da1f6a"
 "foods_sha_id":"c7efa94c6ecbe6dafe685fced7341d9f"
}
"""


@api.route("/food-type", methods=['POST'])
def menutype_foods_add():
    result = {"code": 10000, "value": "", "msg": "添加成功"}
    data = request.data
    data_dict = json.loads(data)
    print(data_dict)

    data_dict['sha_id'] = util.MD5(data_dict['menu_sha_id'] + data_dict['foods_sha_id'])

    cols = data_dict.keys()
    vals = data_dict.values()

    sql = "INSERT INTO %s (%s) VALUES(%s)" % (__table__,
                                              ",".join(cols), ",".join(["%s"] * len(vals))
                                              )
    print(sql)
    print(vals)
    try:
        dbManager.add(sql, tuple(vals))
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result


"""
删除
"""


@api.route("/food-type/<sha_id>", methods=['DELETE'])
def menutype_foods_del(sha_id):
    result = {"code": 10000, "value": "", "msg": "删除成功"}

    condition = {'sha_id': sha_id}

    try:
        dbManager.delete(__table__, condition)
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result
