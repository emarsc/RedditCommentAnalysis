#Collecting real-time comments from reddit
"""TODO:
	-GUI
	-Monitoring thread
	-Clean exit
	-Optimizations
	-Multiprocess queuing
"""
import praw
import store

reddit=praw.Reddit(client_id='dZsi4V3pYz5jVw', client_secret=None, user_agent="Comment Comparison")
subreddits=reddit.subreddit("all") #Subreddits to scrape from.  EX: reddit.subreddit('worldnews+politics+news')


def get_comments(numcomments=100):
	comments=[]
	i=0
	commentStream=subreddits.stream.comments()
	for comment in commentStream:
		i+=1
		comments.append({'id': comment.id,
				'body': comment.body,
				'subreddit_id': comment.subreddit_id,
				'submission_id': comment._extract_submission_id()})
		if i==numcomments:
			break
	return comments

def collect():
	while True:
		comments=get_comments()
		store.store_data(comments)
		print(store.stats())

if __name__=="__main__":
	#No memory buffering. Performance will decrease over time.
	#Ctrl-c to exit  
	collect()

