import time
import redis
import json

from flask import Flask, Response, request

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/kv/<string:i>/<string:k>', defaults={'v': None}, methods=['POST', 'GET', 'DELETE', 'PUT'])
@app.route('/kv/<string:i>/<string:k>/<string:v>', methods=['POST', 'PUT'])
def kv(i: str, k: str, v: str):
    """
    Key-Value Store using Redis
    """
    status = 200
    method = request.method

    if v is None and method in ['POST', 'PUT']:
        return Response(json.dumps({"id": i, "error": "Value parameter is required", "method": method}),
                        status=400, mimetype='application/json')

    if v is not None and method in ['GET', 'DELETE']:
        return Response(json.dumps({"id": i, "error": "Value parameter does not apply", "method": method}),
                        status=400, mimetype='application/json')

    if method == 'GET':
        rv = redis_client.get(k)
        if rv is not None:
            rv = rv.decode("utf-8")
        else:
            status = 404
        response = {"request_id": i, "request_key": k, "response_value": rv, "method": method}

    elif method in ['POST', 'PUT']:
        redis_client.set(k, v)
        response = {"request_id": i, "request_key": k, "request_value": v, "method": method}

    elif method == 'DELETE':
        redis_client.delete(k)
        response = {"request_id": i, "request_key": k, "method": method}

    return Response(json.dumps(response), status=status, mimetype='application/json')


if __name__ == '__main__':
    can_ping = False
    while not can_ping:
        try:
            can_ping = redis_client.ping()
        except Exception as ex:
            print('Cannot connect to redis')
            time.sleep(5)

    app.run(debug=True, host="0.0.0.0", port=80)
