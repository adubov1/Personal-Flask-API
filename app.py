from flask import Flask, jsonify
import requests
import yaml
import json
from flask_cors import CORS

with open("cta_key.yml", 'r') as stream:
    key = yaml.load(stream)["key"]

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

def URL(rt, stpid):
    return (f'http://ctabustracker.com/bustime/api/v2/getpredictions?key={key}&rt={rt}&stpid={stpid}&format=json')

r = requests.get(url = URL(22, 1836))
print(r.text)
print(URL(22, 1836))

@app.route('/ttdem', methods=['GET'])
def ttdprds():
    d = requests.get(url = URL(22, 1836))
    return jsonify({'prd': json.loads(str(d.text))})

@app.route('/tsdem', methods=['GET'])
def tsdprds():
    d = requests.get(url = URL(36, 1836))
    return jsonify({'prd': json.loads(str(d.text))})

@app.route('/ttdiv', methods=['GET'])
def ttvprds():
    d = requests.get(url = URL(22, 1899))
    return jsonify({'prd': json.loads(str(d.text))})

@app.route('/tsdiv', methods=['GET'])
def tsvprds():
    d = requests.get(url = URL(36, 5395))
    return jsonify({'prd': json.loads(str(d.text))})




if __name__ == '__main__':
    app.run(debug=True)
