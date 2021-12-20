from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/', template_folder='templates', static_folder='static')

from .import models, routes