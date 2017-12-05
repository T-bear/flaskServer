import os, datetime
import time
from twitter import *
from flask import Flask, request, render_template, redirect, abort, flash, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)   # create our flask app

# configure Twitter API
twitter = Twitter(
    auth=OAuth(('702963961071837184-dRXZpnnxbPM7VqKIksUmeEnmNhDgoC5'),('3zYdWmN1a9Rbq4zcFi0GIw2fndKWDHUHi5BIhzQ60WgA9'),
                      ('DLxh35KBRYX9zFb5J4c3Wa1WZ'),('At752vGyCIWkA54FRYzhZN8mDosgOttjklBD69fJ5RRbO9wnwf'))
    )
app.config["MONGO_DBNAME"] = "sensor_data"
app.config["MONGO_URI"] = "mongodb://apanappe11:daldaloo11@ds123136.mlab.com:23136/sensor_data"
mongo = PyMongo(app)


@app.route('/')
def main():
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")

	# fetch 3 tweets from my account
	myTweets = twitter.statuses.user_timeline(count=10)
	

	templateData = {
		'title' : 'My last 10 tweets',
		'myTweets' : myTweets,
		'time' : timeString
	}

	return render_template('main.html', **templateData)

@app.route('/getData', methods=['GET'])
def get_all_data():
	data = mongo.db.data
	output = []
 	print output
 	for d in data.find():
		output.append(d["value"])
	return render_template('index', output = output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
