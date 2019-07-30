from app import app
from flask import Flask, render_template, flash, redirect, request, url_for, send_from_directory
from app.darknet.goroom import GoRoom
from app.keywordsform import KeywordsForm
from app.labrecommend import LabRecommend
from app.routerecommend import RouteRecommend
import time
import io
import pandas as pd
import unicodecsv as csv
import json
from io import open

app.config.from_object(__name__)
app.config['SECRETKEY']='65a6b5e4a3204bdd87adb7b1a98eafaa'

goroom_class = None
labr_class = None
route_class = None
number_of_people = 0

@app.route('/')
@app.route('/index')
def index():
    return render_template('counthome.html')

@app.route('/uploads/<path:filename>')
def download_file(filename):
	return send_from_directory('/home/ec2-user/web/app/darknet/room/',filename, as_attachment=True)

@app.route('/buildinga')
def buildinga():
	global goroom_class
	global number_of_people

	if goroom_class == None:
		goroom_class = GoRoom()

	number_of_people = goroom_class.main_goroom()

	# return render_template('buildinga.html')
	return render_template('buildinga.html',nop=number_of_people)


@app.route('/gochat')
def gochat():
	return render_template('chatbothome.html')

@app.route('/goschedule', methods=['GET', 'POST'])
def goschedule():
	# form = KeywordsForm()
	# if request.method == 'POST':
	# 	result = request.form
	# 	print(result)
	# 	print(result.get('data'))
	# 	return redirect(url_for('confirmationroute',data = result.get('data')))
	return render_template('schedulehome.html')

@app.route('/confirmationroute', methods=['GET', 'POST'])
def confirmationroute():
	if request.method == 'POST':
		data = request.form
		with open('/home/ec2-user/web/app/keyword.txt', 'w', encoding='utf-8') as f:
			for key, value in data.items():
				f.write(value + "\n")
		return render_template("confirmationkeywords.html",data = data)
	return render_template('confirmationkeywords.html', data=data)

	
@app.route('/recommendedroute')
def recommendedroute():
	# global goroom_class
	# global number_of_people
	global labr_class
	global route_class

	# if goroom_class == None:
	# 	goroom_class = GoRoom()

	# if number_of_people == 0:
	# 	number_of_people = goroom_class.main_goroom()

	lab_data = pd.read_csv('/home/ec2-user/web/app/labdata.csv')
	lab_data.loc[lab_data["Room"]=="A309","People"] = str(number_of_people)
	lab_data.to_csv('/home/ec2-user/web/app/labdata.csv',index=False)	

	if labr_class == None:
		labr_class = LabRecommend()

	room_number, lab_name = labr_class.main_lab()

	if route_class == None:
		route_class = RouteRecommend()

	route_result = route_class.main_route()

	return render_template('recommendroute.html', room_number = room_number, lab_name = lab_name, route_result = route_result)