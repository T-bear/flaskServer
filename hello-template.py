
import os
import time
from twitter import *
from flask import Flask, render_template, redirect, abort, flash, jsonify
import datetime

app = Flask(__name__)

# configure Twitter APi
twitter = Twitter(
           auth=OAuth(('702963961071837184-dRXZpnnxbPM7VqKIksUmeEnmNhDgoC5'),('3zYdWmN1a9Rbq4zcFi0GIw2fndKWDHUHi5BIhzQ60WgA9'),
                      ('DLxh35KBRYX9zFb5J4c3Wa1WZ'),('At752vGyCIWkA54FRYzhZN8mDosgOttjklBD69fJ5RRbO9wnwf')) 

          )

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'Pi-server',
      'time': timeString
      }

    #fetch 3 tweets from my account
myTweets = twitter.statuses.user_timeline(count=10)

	 #fetch 3 tweets from ITP_NYU
itpTweets = twitter.statuses.user_timeline(screen_name='itp_nyu', count=10)
	
app.logger.debug(itpTweets)

templateData = {
   'title' : 'My last three tweets',
   'myTweets' : myTweets,
   'itpTweets' : itpTweets
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)
