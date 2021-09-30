import json
from flask import Flask, jsonify, request, Response

from .services import retrieve_orders, create_order

app = Flask(__name__)

content_type_json: object = {'Content-Type': 'application/json'}

@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/orders/computers', methods = ['POST'])
def create_order_computers():
    body_value = request.json
    return jsonify(create_order(body_value))


@app.route('/api/orders/computers', methods=['GET'])
def get_orders_computers():
    return jsonify(retrieve_orders())


if __name__ == '__main__':
    app.run()
