from flask import Blueprint,url_for
from werkzeug.utils import redirect
bp=Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'hello, Pybo'

@bp.route('/')
def index():
    #내림차순
    return redirect(url_for('question._list'))
