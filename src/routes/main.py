from flask import Blueprint, render_template

from src.extensions import db
from src.models import Donated

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index.html')
def index():
    return render_template('index.html')
