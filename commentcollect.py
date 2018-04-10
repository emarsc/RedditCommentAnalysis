import praw
import time
import json
import datetime
import os
import sys

#Reddit comment collector
#Collects comments, their score, and submission title from specified subreddit
reddit = praw.Reddit(client_id="dZsi4V3pYz5jVw", client_secret=None, user_agent="comment scraper")


if not os.path.exists('commentdata'):
	os.makedirs('commentdata')


def get_hot(subname, num_posts=20):
	subreddit=reddit.subreddit(subname)
	submissions=subreddit.hot(limit=num_posts)
	return submissions

def collect_submission(submission):
	submission.comments.replace_more(limit=None)
	commentdata={}
	commentdata['post']=submission.title
	comments=[]
	commentdata['comments']=comments
	for c in submission.comments:
		comments.append([c.body, c.score])
	return commentdata

def save_data(data):
	with open('commentdata/'+str(datetime.datetime.today())+'.json', 'w+') as file:
		json.dump(data, file)
	file.close()



if __name__=='__main__':

	subname='worldnews'
	if len(sys.argv)>1:
		subname=sys.argv[1]

	subreddit=reddit.subreddit(subname)
	submissions=subreddit.hot(limit=16)

	data=[]
	i=0
	for submission in submissions:
		i+=1
		commentdata=collect_submission(submission)
		data.append(commentdata)
		print('collected '+submission.title)
		if(i%4==0):
			save_data(data)
			data=[]

	if len(data)>0:
		save_data(data)

