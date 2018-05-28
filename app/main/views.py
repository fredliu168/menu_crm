# -*- coding: utf-8 -*-
from flask import render_template, sessions, redirect, url_for
from . import main
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template

from app.model.menuType import *

photos = UploadSet('PHOTO')

@main.route('/photo/<name>')
def show(name):
    if name is None:
        return None
    url = photos.url(name)
    return render_template('show.html', url=url, name=name)


@main.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return redirect(url_for('main.show', name=filename))
    return render_template('upload.html')


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
