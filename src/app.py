from flask import Flask, render_template
from hackernews_tidal import *
from twitter_tidal import *
import tweepy

app = Flask(__name__)

# sample dashboard constants to get this working before I try using an actual database
dashboard = 'Trendy Software Developer'
widgets = []

hn_user = 'dazebra'
twitter_user = 'kanyewest'
profile_data = find_profile(hn_user)
submission_data = find_submissions(hn_user)
comment_data = find_comments(hn_user)
tweets = get_tweets(twitter_user, 10)

@app.route("/")

def index():
    return render_template('index.html', dashboard_name = profile_data[0][0], karma = profile_data[0][2], date = profile_data[0][1], dashboard_current = dashboard, sample_tweet = tweets[1].text, twitter_name = twitter_user)

# gets desired profile information
@app.route("/hackernews_profile/")
def hackernews_profile():
    return "username: " + str(profile_data[0][0]) + "\n" + "date created: " + str(profile_data[0][1]) + "\n" + "karma: " + str(profile_data[0][2])

@app.route("/add_widget/")
def add_widget():
    #load widget creation page
    temp = 42 # to do

if __name__ == "__main__":
    app.run()


#       ideas to make this work:
#       - accept the fact that routing will make this a multi-page application for simplicity
#       - use AJAX requests to load onto the same page, not React
#
#
#
#
