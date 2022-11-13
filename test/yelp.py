from flask import Flask
from flask import request
import requests

app = Flask(__name__)
YELP_TOKEN = "ILTWEKhCXbDvJ7_ZgdZNK7TS-06kb2Rr5PECW6V7a6i0PsJ7V5eIH_ecOhFskhMdyFoWJ_5xWFMFqwR0_V1sX1m2DTsLoe_7KypkckEdqDFJq9s8Cpwdfvk-nABwY3Yx"


@app.route('/')
def index():
    return 'Web App with Python Flask!'


@app.route('/test')
def test():
    url = "https://api.yelp.com/v3/businesses/search"
    params = {
        'term' : request.args.get('term'),
        'location' : 'SF',
        'limit' : 10
    }
    headers = {
        'Authorization': 'Bearer {}'.format(YELP_TOKEN)
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    return response.json()


app.run(host='0.0.0.0', port=81)
