
https://crazyj.tistory.com/172

# install python3

# install


pip install flask
pip install flask_restful


# Server Program 작성





# Server Start Shell작성(testsvr.py)

from flask import Flask, request
from flask_restful import Resource, Api
from flask.views import MethodView

import logging
import json, base64

import os, sys
import datetime
import threading, time

app = Flask(__name__)
api = Api(app)

log = logging.basicConfig(filename = 'testsvr.log', level=logging.INFO)

~~ Class 내용 작성~~



api.add_resource(apitest1, '/apitest1')
api.add_resource(sum, '/sum')

port = 18899

if __name__ == '__main__':
	print('Start Server...port=', port)
	logging.info('start server')
	app.run(host='0.0.0.0', port=port, debug=True)




# testsvr.py
#! /bin/bash

# [python env path...]/bin/python testsvr.py
# linux ex)
/opt/anaconda3/envs/tensorflow/bin/python testsvr.py
#windows command ex)
# c:\python37\scripts\python testsvr.py


# Server 구동
python testsvr.py
