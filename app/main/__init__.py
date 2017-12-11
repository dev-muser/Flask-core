from flask import Blueprint

main = Blueprint('main', __name__, template_folder='/template/main')

from .import controllers
