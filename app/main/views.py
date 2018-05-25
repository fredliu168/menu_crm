# -*- coding: utf-8 -*-
from flask import render_template, sessions, redirect, url_for
from . import main

from app.model.menuType import *


@main.route('/', methods=['GET', 'POST'])
def menu_type_index():
    # 菜单分类配置
    return render_template('menu-type.html')


@main.route('/foods', methods=['GET', 'POST'])
def foods_index():
    # 菜品配置
    return render_template('foods.html')


@main.route('/menu-type-foods/<type_sha_id>', methods=['GET', 'POST'])
def menu_type_foods_index(type_sha_id):
    # 菜单分类对应的菜品
    menuType = MenuType()
    menuType.get(type_sha_id)
    print(menuType.title)
    return render_template('menu-type-foods.html', type_sha_id=type_sha_id, menu_type_title=menuType.title)
