from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask.views import MethodView
from flask_cors import CORS

import logging
import json, base64

import os, sys
import datetime
import threading, time

import lotto_machine_action as lma

app = Flask(__name__)
app.config.from_object(__name__)

#https://stackabuse.com/single-page-apps-with-vue-js-and-flask-ajax-integration/

cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

nums = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21', '22','23','24', '25', '26', '27','28','29','30','31','32','33','34','35','36','37','38','39','40','41', '42','43', '44', '45']

log = logging.basicConfig(filename='testsvr.log', level=logging.INFO)

#active_machine = lma.lotto_machine_action(nums)


class pop_one(MethodView):
	active_machine = None

	def __init__(self):
		self.active_machine = lma.lotto_machine_action(nums)
	
	def get(self):
		print(len(self.active_machine.machine.myBasket))
		return self.active_machine.pop_ball()
	
class pop_all(MethodView):	
	active_machine = None

	'''
	def __init__(self):
		print(nums)
		self.active_machine = lma.lotto_machine_action(nums)
	'''

	def __init__(self):
		data = request.args
		balls = data.get('balls').split(',')
		
		self.active_machine = lma.lotto_machine_action(balls)

	def __del__(self):
		del self.active_machine

	def get(self):
		data = request.args
		print('recv:', data)
		cnt = data.get('extract_count')
		
		if cnt:
			extract = self.active_machine.pop_balls(int(cnt))
			print(extract)	
			return jsonify(message="pop_all", category="sucess", status=200, result=extract)

	def post(self):
		return self.get()

class pop_test(MethodView):
	def get(self):
		print('test ok')
		return 'test ok'


@app.route('/ping', methods=['GET', "OPTIONS"])
def ping_pong():
	#my_res =app.Response()
	
	#my_res = jsonify(message="1", category="sucess", status=200, data="1")
	#my_res.headers.add("Content-Type", "application/json")
	#my_res.headers.add("Access-Control-Allow-Origin", "*")
	print("PONG")
	return  jsonify(message="1", category="sucess", status=200, result="PONG")

@app.route("/", methods=["GET","OPTIONS"])
def index():
	response = jsonify({"order_id": 123, "status": "shipped"})
	response.headers.add("Access-Control-Allow-Origin", "*")
	return response


api.add_resource(pop_one, '/pop_one')
api.add_resource(pop_all, '/pop_all')
api.add_resource(pop_test, '/pop_test')

port = 18899

if __name__=='__main__':
	print('Start Server ... Port=', port)
	logging.info('start server')
	app.run(host='0.0.0.0', port=port, debug=True)
