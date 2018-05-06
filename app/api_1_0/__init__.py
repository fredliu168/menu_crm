from flask import Blueprint

api = Blueprint('api', __name__)

from . import menu_type,foods,menutype_foods, images,tables,order
