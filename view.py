# main.py

from flask import Blueprint, render_template, request, flash
from . import db
from flask_login import login_required, current_user

view = Blueprint('view', __name__)


@view.route('/')
def index():
    return render_template('index.html')


