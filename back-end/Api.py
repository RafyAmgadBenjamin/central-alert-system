from bottle import route, run, error, template, abort
from random import randint
import random
import redis
import json
from bottle import hook, request, response
from bottle import post, get, put, delete
import bottle
import base64
import time


#  configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

# the decorator


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


app = bottle.app()


@app.route('/api/alerts/get-alerts/<type>', method=['OPTIONS', 'GET', 'POST'])
@enable_cors
def get_alerts(type):
    """
    Get alerts depending on the environment
    """
    data = get_data()
    dataList = data["alerts"]
    if(type.upper() != "ALL"):
        filterData = [
            item for item in dataList if item['environment'].upper() == type]
    else:
        filterData = dataList
    time.sleep(4)
    return {"alerts": filterData}


def get_data():
    with open('/home/rafy/svelte/central-alert-system/back-end/data.json') as json_file:
        data = json.load(json_file)
        # print(data)
        return data


@app.route('/api/alerts/add-alert', method=['OPTIONS', 'GET', 'POST'])
@enable_cors
def add_alert():
    """
    Add the alert to the data base
    """
    alert = json.dumps(request.json['alert'])
    encodedAlerts = stringToBase64(alert)

    generatedVal = str(generate_random_no())
    add_alert_redis(radndomNo=generatedVal,
                    data=encodedAlerts)
    return {"alertId":generatedVal}



def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')


def add_alert_redis(radndomNo, data):
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port,
                              password=redis_password, decode_responses=True)

        # step 4: Set the data in Redis
        r.set(radndomNo, data)
        print("from redis " + r.get(radndomNo))

        # step 5: Retrieve the data message from Redis
    except Exception as e:
        print(e)


def generate_random_no():

    random.seed(a=None)
    return randint(0, 1000000)  # randint is inclusive at both ends

run(host='localhost', port=8080, debug=True)
