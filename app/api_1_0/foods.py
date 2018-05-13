import re
from app import util
from app.model.menuType import *
from . import api
import json
from flask import request

"""
获取foods
"""
@api.route("/food", methods=['GET'])
def get_foods():
    result = {"code": 10000, "value": "", "msg": ""}
    sql = """select * from foods t order by t.food_index"""

    food = dbManager.exec_sql(sql)

    result["value"] = food
    result["msg"] = "获取数据成功"

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