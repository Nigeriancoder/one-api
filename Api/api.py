from flask import Blueprint
from Db.db import Db

api = Blueprint('api', __name__)


@api.route('/')
def get_table():

    db = Db()
    table = db.get_table('counter')

    for i in table:
        print(i.count)
