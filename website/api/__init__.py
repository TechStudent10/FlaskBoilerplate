from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/hello')
def helloWorld():
    return jsonify(result="bye")