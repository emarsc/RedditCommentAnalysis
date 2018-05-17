#Storing comment data without duplicates
"""TODO:
	-Optimzations:
		-Main memory buffering
		-File buffering
		-Commit intervals
		-Trie structure to search for duplicates
		-Branch minimization
		-Benchmark
	-Data:
		-subreddit title
		-submission title
		-submission url
	-Reaccess functionality
"""
import json
import dataSetup
import atexit

with open('data.json', 'r') as file:
	data=json.load(file)
file.close()


commentID=data['commentID']
submissionID=data['submissionID']
subredditID=data['subredditID']
commentBody=data['commentBody']
submissionMeta=data['submissionMeta']
subredditMeta=data['subredditMeta']

def commit():
	with open('data.json', 'w') as file:
		json.dump(data, file)
	file.close()

atexit.register(commit)

def filter(comments, submissions, subreddits):
	i=0
	while (i<len(comments)):
		if comments[i]['id'] in commentID:
			comments.pop(i)
		else:
			i+=1
	i=0
	while (i<len(submissions)):
		if submissions[i]['id'] in submissionID:
			submissions.pop(i)
		else:
			i+=1
	i=0
	while (i<len(subreddits)):
		if subreddits[i]['id'] in subredditID:
			subreddits.pop(i)
		else:
			i+=1


def store_data(comments):
	submissions=[]
	subreddits=[]
	for comment in comments:
		if comment['subreddit_id'] not in subreddits:
			subreddits.append({'id': comment['subreddit_id']})
		if comment['submission_id'] not in submissions:
			submissions.append({'id': comment['submission_id']})
	filter(comments, submissions, subreddits)
	for comment in comments:
		commentID.append(comment['id'])
		commentBody.append(comment['body'])
	for submission in submissions:
		submissionID.append(submission['id'])
	for subreddit in subreddits:
		subredditID.append(subreddit['id'])

def stats():
	return {'numComments': len(commentID), 'numSubmissions': len(submissionID), 'numSubreddits': len(subredditID)}

