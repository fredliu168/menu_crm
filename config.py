# -*- coding: utf-8 -*-
# 配置文件
# 2018.3.13
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# 注意 配置需要大写才能加到配置项里去 2018.3.30
class Config:
    # image_dir = '{}/upload/images'.format(basedir)  # 图片的存储路径
    # ROOM_IMG_DIR = '{}/room'.format(image_dir)  # 保存房产图片的路径
    # AVATAR_DIR = '{}/avatar'.format(image_dir)  # 保存头像路径
    # DEFAULT_ROOM_DIR = '{}/default_room.jpg'.format(image_dir)  # 默认房屋图片
    # DEFAULT_AVATAR_DIR = '{}/default_avatar.jpg'.format(image_dir)  # 默认用户头像图片
    # BANNER_DIR = '{}/banner/banner.png'.format(image_dir)
    # # 获取资源文件
    # SOURCE_IMG_DIR = '{}/source'.format(image_dir)
    DEFAULT_FOOD_IMG_DIR = '{}/upload/images/source/default.jpg'.format(basedir)  # 默认用户头像图片
    UPLOADED_PHOTO_DEST = '{}/upload/images'.format(basedir)  # 图片的存储路径
    UPLOADED_PHOTO_ALLOW = IMAGES

    # mysql
    DB_PWD = 'fred123456'
    DB_DATABASE = 'menu_book'
    DB_USER = 'root'
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306

    @staticmethod
    def init_app(app):
        pass


class DockerConfig(Config):
    DB_HOST = 'db'

    # mysqlserver

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {'docker': DockerConfig,
          'default': ProductionConfig}
