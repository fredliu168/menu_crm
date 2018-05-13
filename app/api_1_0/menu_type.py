from app import util
from app.model.menuType import *
from . import api
import json
from flask import request

"""
获取菜单分类
"""

@api.route("/menu-type", methods=['GET'])
def get_menutype():
    result = {"code": 10000, "value": "", "msg": ""}
    sql = """select * from menu_type t order by t.type_index"""

    menu_types = dbManager.exec_sql(sql)

    result["value"] = menu_types
    result["msg"] = "获取数据成功"

    return result


"""
添加
{
 "title":"菜单名称"
}
"""


@api.route("/menu-type", methods=['POST'])
def menutype_add():
    result = {"code": 10000, "value": "", "msg": "添加成功"}
    data = request.data
    data_dict = json.loads(data.decode('utf-8'))

    data_dict['sha_id'] = util.MD5(data_dict['title'])

    cols = data_dict.keys()
    vals = data_dict.values()

    sql = "INSERT INTO menu_type (%s) VALUES(%s)" % (
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


@api.route("/menu-type/<sha_id>", methods=['PUT'])
def menutype_modify(sha_id):
    result = {"code": 10000, "value": "", "msg": "修改成功"}

    data = request.data
    data_dict = json.loads(data)

    data_dict['sha_id'] = util.MD5(data_dict['title'])

    condition = {'sha_id': sha_id}

    try:
        dbManager.update('menu_type', data_dict, condition)
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result


"""
删除
"""


@api.route("/menu-type/<sha_id>", methods=['DELETE'])
def menutype_del(sha_id):
    result = {"code": 10000, "value": "", "msg": "删除成功"}

    condition = {'sha_id': sha_id}

    try:
        dbManager.delete('menu_type', condition)
    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result
