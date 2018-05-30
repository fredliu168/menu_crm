# -*- coding: utf-8 -*-
# 图片类
# 20180313

import json
import os

import requests
from flask import current_app

from .. import dbManager
from .. import util
import time


class Image(object):

    def __init__(self):
        self.food_sha_identity = ''  # 房屋sha_identity外键
        self.sha_id = ''  # 图片sha_id
        self.name = ''  # 图片名称
        self.post_time = ''  # 上传照片时间
        self.path = ''  # 图片存放路径





    def setFoodImg(self, food_sha_id):
        # 保存到物品图片
        self.sha_id = util.MD5(self.path)
        dbManager.insert('food_images', insert_data=[
            {"food_sha_id": food_sha_id, "img_sha_id": self.sha_id}])

    def getImg(self, sha_id):
        sql = """select * from images t where t.sha_id='{sha_id}'""".format(sha_id=sha_id)

        _image = dbManager.exec_sql(sql)

        if len(_image) > 0:
            return _image[0]["path"]
        return None

    def saveDb(self):
        self.sha_id = util.MD5(self.path)
        self.post_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 保存内容到数据库
        dbManager.insert('images', insert_data=[
            {"sha_id": self.sha_id, "post_time": self.post_time,
             "path": self.path}])

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


if __name__ == '__main__':
    roomImage = RoomImage()

    roomImage.post_time = '2018-03-13 08:50:00'
    roomImage.name = "https://att.dehuaca.com/house/201803/05/105924f4o3on9n4i56t496.jpg"
    roomImage.room_sha_identity = '841e61348cc394645fd19d6f65621f6b'

    # name = roomImage._fetch()
    # roomImage._saveDb()

    roomImage.save()

    # print(name)

    # post_time = '2018-03-13 08:50:00'
    #
    # date_post_time = datetime.datetime.strptime(post_time, '%Y-%m-%d %H:%M:%S')
    #
    # post_time = date_post_time.strftime('%Y-%m-%d')
    #
    # print(post_time)
