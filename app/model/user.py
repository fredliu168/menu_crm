# -*- coding: utf-8 -*-
# 用户类
# 20180313
import json
import os
import requests
from app import util
from .. import dbManager
from .. import config
from flask import current_app


class User():
    # 用户信息
    def __int__(self):
        self.sha_id = ''
        self.nickName = ''  # 用户昵称
        self.gender = 0  # 用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
        self.city = ''  # 用户所在城市
        self.province = ''  # 用户所在省份
        self.country = ''  # 用户所在国家
        self.language = ''  # 用户的语言，简体中文为zh_CN
        self.unionId = ''  # 用户信息
        self.phoneNumber = ''  # 用户绑定的手机号（国外手机号会有区号）
        self.purePhoneNumber = ''  # 没有区号的手机号
        self.countryCode = ''  # 区号
        self.password = ''  # 用户登录密码
        self.avatarUrl = ''  # 用户头像信息
        self.description = ''  # 其他描述信息
        self.point = 0  # 积分


    def get_user(self,sha_id):
        sql = """select * from user t where t.sha_id='{sha_id}'""".format(sha_id=sha_id)

        user_dic = dbManager.exec_sql(sql)

        return self.dict2obj(user_dic[0])

    def dict2obj(self,d):
        if isinstance(d, User):
            d = [self.dict2obj(x) for x in d]
        if not isinstance(d, dict):
            return d
        for k in d:
            self.__dict__[k] = self.dict2obj(d[k])
        return self

    def save_avatar(self, url):
        # 保存用户头像

       pass

        # @staticmethod
        # def save_user2db(users_dic):
        #     # 把数据保存到数据库
        #     insert_data = []
        #
        #     for user_dic in users_dic.values():
        #         #print(user_dic)
        #         user = User()
        #         util.dict2obj(user_dic, user)
        #         #print(user.avatar)
        #
        #         user.avatar = save_avatar(user.avatar)
        #         insert_data.append(json.loads(user.toJSON()))
        #
        #     dbManager.insert('user', insert_data=insert_data)

    def save(self):
      pass
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def descript(self):
        print(self.sha_id)
        print(self.nickName)
        print(self.purePhoneNumber)
