import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS', \
                     client_secret='SECRET_KEY_27_CHARS ', \
                     user_agent='YOUR_APP_NAME', \
                     username='YOUR_REDDIT_USER_NAME', \
                     password='YOUR_REDDIT_LOGIN_PASSWORD')

subreddit = reddit.subreddit('SUBREDDIT_NAME')
posts = { "title":[], \
        "body":[], \
        "id":[], \
        "date:":[], \
        "url:"[]}

def get_date(date):
    return dt.datetime.fromtimestamp(date)

_timestamp = posts["date"].apply(get_date)
posts = posts.assign(timestamp = _timestamp)

for submission in subreddit.new(limit=500):
    posts["title"].appened(submission.title)
    posts["body"].append(submission.selftext)
    posts["id"].append(submission.id)
    posts["url"].append(submission.url)
    posts["date"].append(submission.created)
    posts = pd.DataFrame(posts)
