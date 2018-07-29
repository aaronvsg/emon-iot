#!flask/bin/python
from flask import Flask
app = Flask(__name__)
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/postjson', methods=['POST'])
def post():
    print(request.is_json)
    content = request.get_json()
    #print(content)
    print(content['id'])
    print(content['name'])
    return 'JSON posted'
app.run(host='127.0.0.1', port=5000)