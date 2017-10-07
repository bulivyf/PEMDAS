from flask import Flask
from flask_cors import CORS, cross_origin
import random

import json
from time import sleep

# get this object
from flask import Response

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.debug = True

@app.route('/randnums',methods=['GET'])
def index():
    r = [random.randint(1, 10) for i in range(random.randint(1, 10))]
    resp = Response(json.dumps(r),  mimetype='application/json')
    resp.status_code = 201
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = '*'
    resp.headers['Access-Control-Allow-Domain'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = True
    sleep(0.15)
    print(r)
    return resp

if __name__ == "__main__":
    app.run()
