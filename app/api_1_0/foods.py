import re
from app import util
from app.model.menuType import *
from app.model.image import *
from app.model.food import *
from . import api
import json
from flask import request

"""
获取foods
"""


@api.route("/food", methods=['GET'])
def get_foods():
    result = {"code": 10000, "value": "", "msg": ""}
    sql = """select * from foods t order by  t.states desc,t.food_index"""

    food_obj = Food()
    _foods = dbManager.exec_sql(sql)

    for food in _foods:
        # print(food['sha_id'])
        images = food_obj.getFoodImg(food['sha_id'])
        #print(images)
        food['images'] = images

        if len(images) >0:
            food['primary_img'] = images[0]['url']
        else:
            food['primary_img'] = '/api/v1.0/image/default'




    result["value"] = _foods
    result["msg"] = "获取数据成功"

    return result


@api.route("/food/<sha_id>/<enable>", methods=['GET'])
def enable_foods(sha_id, enable):
    """

    :param sha_id:
    :param enable:
    :return:
    """
    result = {"code": 10000, "value": "", "msg": ""}

    #sql = """update foods set states = {state} where sha_id='{sha_id}'""".format(state=enable, sha_id=sha_id)

    #print(sql)
    dbManager.update('foods',{'states':enable},{'sha_id':sha_id})

    #result["value"] = food
    result["msg"] = "更新数据成功"

    return result


"""
添加
{
 "title":"全猪肉",
 "price":60,
 "unit":"份",
 "total_num":10,
 "description":"测试"
}
"""


@api.route("/food", methods=['POST'])
def foods_add():
    result = {"code": 10000, "value": "", "msg": "添加成功"}
    data = request.data
    data_dict = json.loads(data.decode('utf-8'))

    print(data_dict)

    print(data_dict.keys)

    if data_dict == {} or "title" not in data_dict or len(data_dict['title'].strip()) == 0:
        result['code'] = -10000
        result['msg'] = "名称不能为空"
        return result

    if "price" not in data_dict:
        result['code'] = -10000
        result['msg'] = "价格不能为空"
        return result

    if "total_num" not in data_dict:
        result['code'] = -10000
        result['msg'] = "数量不能为空"
        return result

    if "unit" not in data_dict:
        result['code'] = -10000
        result['msg'] = "单位不能为空"
        return result

    data_dict['sha_id'] = util.MD5(data_dict['title'])

    cols = data_dict.keys()
    vals = data_dict.values()

    sql = "INSERT INTO foods (%s) VALUES(%s)" % (
        ",".join(cols), ",".join(["%s"] * len(vals))
    )

    try:
        dbManager.add(sql, tuple(vals))
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result


"""
修改
"""


@api.route("/food/<sha_id>", methods=['PUT'])
def foods_modify(sha_id):
    result = {"code": 10000, "value": "", "msg": "修改成功"}

    data = request.data
    data_dict = json.loads(data)

    if data_dict == {} or "title" not in data_dict or len(data_dict['title'].strip()) == 0:
        result['code'] = -10000
        result['msg'] = "名称不能为空"
        return result

    if "price" not in data_dict:
        result['code'] = -10000
        result['msg'] = "价格不能为空"
        return result

    if "total_num" not in data_dict:
        result['code'] = -10000
        result['msg'] = "数量不能为空"
        return result

    if "unit" not in data_dict:
        result['code'] = -10000
        result['msg'] = "单位不能为空"
        return result

    data_dict['sha_id'] = util.MD5(data_dict['title'])

    condition = {'sha_id': sha_id}

    try:
        dbManager.update('foods', data_dict, condition)
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result


"""
删除
"""


@api.route("/food/<sha_id>", methods=['DELETE'])
def foods_del(sha_id):
    result = {"code": 10000, "value": "", "msg": "删除成功"}

    condition = {'sha_id': sha_id}

    try:
        dbManager.delete('foods', condition)
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result
