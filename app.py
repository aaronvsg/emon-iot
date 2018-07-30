#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)
from flask import Flask
from flask import request
import requests
import json
app = Flask(__name__)

class Authorization(object):
	def __init__(self, j):
		self.__dict__ = json.loads(j)

@app.route('/connected', methods=['GET'])
def connected():
		response = requests.post('https://test.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sLbBxQYwWqsS2AAcNaKaVTir.Oy9wS8PRdkyiumXI3Pxw1WUingJioe4mncsDhPh8W3knVN2I2gI2DJY&client_secret=8313047119835055425&username=paleteros@incompany.com.dev&password=Paleter@s2018SHqDtt2lP4BkH1VccRnqRtT0')
	    	data = response.json()
	    	print(data)
	    	j = Authorization(response.text)
	    	url = 'https://cs14.salesforce.com/services/apexrest/EMONArduino/PlazaRohrmoser-Connected'
	    	headers = {'Authorization': 'Bearer '+j.access_token}
	    	response2 = requests.get(url,headers = headers)
		return response2.text

@app.route('/disconnected', methods=['GET'])
def disconnected():
		response = requests.post('https://test.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sLbBxQYwWqsS2AAcNaKaVTir.Oy9wS8PRdkyiumXI3Pxw1WUingJioe4mncsDhPh8W3knVN2I2gI2DJY&client_secret=8313047119835055425&username=paleteros@incompany.com.dev&password=Paleter@s2018SHqDtt2lP4BkH1VccRnqRtT0')
	    	data = response.json()
	    	print(data)
	    	j = Authorization(response.text)
	    	url = 'https://cs14.salesforce.com/services/apexrest/EMONArduino/PlazaRohrmoser-Disconnected'
	    	headers = {'Authorization': 'Bearer '+j.access_token}
	    	response2 = requests.get(url,headers = headers)
		return response2.text
app.run(host='0.0.0.0', port=5000)