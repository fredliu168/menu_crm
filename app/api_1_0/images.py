# -*- coding: utf-8 -*-
# 图片数据
# 20180330
from flask import Flask, Response, jsonify, current_app
import re
from app.model.image import *
from . import api
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template
from manage import photos
import time


@api.route("/upload/<foods_sha_id>", methods=['POST', 'GET'])
def upload(foods_sha_id):
    result = {"code": 10000, "value": "", "msg": "上传成功"}
    print('upload:' + foods_sha_id)
    try:
        if request.method == 'POST' and 'file' in request.files:
            filename = photos.save(request.files['file'], time.strftime("%Y-%m-%d", time.localtime()))
            image = Image()
            image.path = filename

            image.saveDb()
            image.setFoodImg(foods_sha_id)  # 保存物品对应关系

            result['value'] = filename
        else:
            result['code'] = -10000
            result['msg'] = "上传失败"

    except Exception as ex:

        code, err_message = ex.args

        result['code'] = -10000
        result['msg'] = err_message

    return result


@api.route("/source/<img_sha_id>")
def source_img(img_sha_id):
    # 获取资源文件
    image = Image()
    path = image.getImg(img_sha_id)

    if path is None:
        return None

    img_local_path = "{}/{}".format(current_app.config['UPLOADED_PHOTO_DEST'], path)

    print(img_local_path)

    img_stream = ''

    print(img_local_path)

    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()

    resp = Response(img_stream, mimetype="image/jpeg")
    return resp


@api.route("/banner")
def banner():
    # 返回标题图片
    img_local_path = "{}".format(current_app.config['BANNER_DIR'])

    img_stream = ''

    print(img_local_path)

    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()

    resp = Response(img_stream, mimetype="image/jpeg")
    return resp


@api.route("/image/<imageid>")
def room_image(imageid):
    """
    返回房间的图片
    :param imageid:
    :return:
    """
    if imageid == 'default':  # 设置默认图片
        img_local_path = current_app.config['DEFAULT_FOOD_IMG_DIR']
    else:

        ret = dbManager.exec_sql("select path from image where name='{name}'".format(name=imageid))
        img_local_path = "{}/{}".format(current_app.config['ROOM_IMG_DIR'], ret[0]['path'])

    img_stream = ''

    print(img_local_path)

    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()

    resp = Response(img_stream, mimetype="image/jpeg")
    return resp


@api.route("/avatar/<imageid>")
def avatar(imageid):
    """
    返回头像
    :param imageid:
    :return:
    """
    if imageid == 'default' or imageid == 'null':  # 设置默认图片
        img_local_path = current_app.config['DEFAULT_AVATAR_DIR']
    else:
        img_local_path = "{}/{}".format(current_app.config['AVATAR_DIR'], imageid)

    print(img_local_path)
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()

    resp = Response(img_stream, mimetype="image/jpeg")
    return resp
