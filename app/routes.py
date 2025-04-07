from flask import Blueprint, request, jsonify
from .services import calculate

calc_bp = Blueprint('calc', __name__)

@calc_bp.route('/')
def hello():
    return "Hello World! salut"

@calc_bp.route('/calc')
def calc():
    a = request.args.get('a')
    b = request.args.get('b')
    op = request.args.get('op')
    try:
        result = calculate(int(a), int(b), op)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

#http://127.0.0.1:5000/calc?a=10&b=5&op=div