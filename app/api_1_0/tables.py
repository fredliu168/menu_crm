from app import util
from app.model.menuType import *
from . import api
import json
from flask import request

__table__ = "restaurant_tables"

"""
获取菜单分类
"""


@api.route("/table", methods=['GET'])
def get_tables():
    result = {"code": 10000, "value": "", "msg": ""}
    sql = """select * from {table} order by `number`""".format(table=__table__)

    tables_info = dbManager.exec_sql(sql)

    result["value"] = tables_info
    result["msg"] = "获取数据成功"

    return result


"""
添加
"""


@api.route("/table", methods=['POST'])
def tables_add():
    result = {"code": 10000, "value": "", "msg": "添加成功"}
    data = request.data
    data_dict = json.loads(data)

    data_dict['sha_id'] = util.MD5(data_dict['title'] + str(data_dict['number']))

    cols = data_dict.keys()
    vals = data_dict.values()

    sql = "INSERT INTO %s (%s) VALUES(%s)" % (__table__,
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


@api.route("/table/<sha_id>", methods=['PUT'])
def tables_modify(sha_id):
    result = {"code": 10000, "value": "", "msg": "修改成功"}

    data = request.data
    data_dict = json.loads(data)

    data_dict['sha_id'] = util.MD5(data_dict['title']+str(data_dict['number']))

    condition = {'sha_id': sha_id}

    try:
        dbManager.update(__table__, data_dict, condition)
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result


"""
删除
"""


@api.route("/table/<sha_id>", methods=['DELETE'])
def tables_del(sha_id):
    result = {"code": 10000, "value": "", "msg": "删除成功"}

    condition = {'sha_id': sha_id}

    try:
        dbManager.delete(__table__, condition)
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result
