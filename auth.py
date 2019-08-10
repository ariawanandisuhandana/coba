from flask import Blueprint, render_template, request, flash
from . import db
from .models import Pemeringkatan2019

auth = Blueprint('auth', __name__)

@auth.route('/peringkat2019', methods=['POST'])
def peringkat2019():
    if request.method == 'POST':
        return render_template('index2.html')
    else:
        flash("Ada Kesalahan, Pastikan Menggunakan URL yang sudah ada")
        return render_template('index.html')