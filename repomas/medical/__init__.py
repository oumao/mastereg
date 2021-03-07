from flask import Blueprint

med = Blueprint('med', __name__)

from . import views

