import json
import datetime
import time
import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


if not os.path.exists('processed'):
	os.makedirs('processed')
	with open('posts.txt', 'w+') as file:
		file.write("")
	file.close()
	with open('words.json', 'w+') as file:
		json.dump([], file)
	file.close()

with open('posts.txt', 'r') as file:
	parsed_posts=file.readlines()
file.close()
words=[]

stop_words=set(stopwords.words('english'))


def process_comment(comment):
	#https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
	comment=comment.lower()
	comment=re.sub(r'[^a-zA-Z ]', '', comment)
	word_tokens=word_tokenize(comment)
	filtered_comment = [w for w in word_tokens if not w in stop_words]
	comment=" ".join(filtered_comment)

	#comment=comment.replace("'", "")
	#comment=comment.replace(",", "")
	#comment=comment.replace(".", "")

	return comment

def process_submission(submission):
	#'submission' has been collected and formated
	comments=submission['comments']
	words=[]
	for i in range(0, len(comments)):
		comments[i][0]=process_comment(comments[i][0])
		words.extend(list(set(comments[i][0].split(" "))))
	words=list(set(words))
	#print(str(words))
	return submission, words

def process_data():
	files=os.listdir('commentdata')
	with open('words.json', 'r') as file:
		words=json.load(file)
	file.close()
	for fname in files:
		with open('commentdata/'+fname, 'r') as file:
			posts=json.load(file)
		file.close()
		for post in posts:
			comments=post['comments']
			for i in range(0, len(comments)):
				comments[i][0]=process_comment(comments[i][0])
				words.extend(list(set(comments[i][0].split(" "))))
				
			parsed_posts.append(post['post'])
		with open('processed/'+str(datetime.datetime.today())+'.json', 'w+') as file:
			json.dump(posts, file)
		file.close()
	with open('posts.txt', 'w') as file:
		for p in parsed_posts:
			file.write(p+'\n')
		file.close()
	word_set=set(words)
	words=list(word_set)
	with open('words.json', 'w') as file:
		json.dump(words, file)
	file.close()

if __name__=='__main__':
	process_data()




