from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import time
import praw

reddit=praw.Reddit(client_id='dZsi4V3pYz5jVw', client_secret=None, user_agent="Comment Comparison")

numCloudComments=1000 #the number of comments to consider at any given time
cloudComments=[]
sw=set(stopwords.words("english"))
subreddits=['worldnews', 'politics']
subs=reddit.subreddit("+".join(subreddits))
wordDict={}
trantab=str.maketrans('', '', string.punctuation)
	
def comment_tokens(comment):
	comment=comment.translate(trantab)
	tokens=word_tokenize(comment)
	i=0
	numtokens=len(tokens)
	while i<numtokens:
			if tokens[i] in sw:
					tokens.pop(i)
					numtokens-=1
			else:
					i+=1
	return tokens

def get_comments(numcomments):
	comments=[]
	i=0
	commentStream=subs.stream.comments()
	for comment in commentStream:
		comments.append(list(comment_tokens(comment.body)))
		i+=1
		#print(str(i))
		if i%100==0:
			print(str(i))
		if i>numcomments:
			return comments
	
def add_comments(numcomments):
	newComments=get_comments(numcomments)
	for comment in newComments:
		for word in comment:
			if word in wordDict.keys():
				wordDict[word]=wordDict[word]+1
			else:
				wordDict[word]=1
	cloudComments.extend(newComments)
	
		
def remove_comments(numcomments):
	for i in range(0, numcomments):
		comment=cloudComments.pop(0)
		for word in comment:
			frequency=wordDict.pop(word, None)
			frequency-=1
			if frequency:
				wordDict[word]=frequency
		
def find_top_words(numcomments=10):
	def find_min(word_list):
		min=wordDict[word_list[0]]
		minWord=word_list[0]
		for word in word_list:
			if wordDict[word]<min:
				min=wordDict[word]
				minWord=word
		return min, minWord
		
	words=list(wordDict.keys())
	topWords=words[0:numcomments]
	min, minWord=find_min(topWords)
	for w in words:
		if wordDict[w]>min:
			topWords.remove(minWord)
			topWords.append(w)
			min, minWord=find_min(topWords)
	return topWords
	
def test():
	for i in range(0, 5):
		add_comments(100)
		
	"""for i in range(0, 10):
		start=time.clock()
		topWords=find_top_words()
		for word in topWords:
			print(word+" "+str(wordDict[word]))
		remove_comments(100)
		add_comments(100)
		end=time.clock()
		print("Time: "+str(start-end))"""
	
	import matplotlib.pyplot as plt
	import matplotlib.animation as anim
	
	fig, ax=plt.subplots()
	yval=[]
	
	def update(i):
		remove_comments(100)
		add_comments(100)
		topWords=find_top_words()
		yval=[]
		ax.clear()
		ax.set_ylabel("frequency")
		ax.set_xlabel("word")
		ax.set_xticks(list(range(0, 10)))
		ax.set_xticklabels(topWords)
		print(str(topWords))
		for word in topWords:
			yval.append(wordDict[word])
	
		ax.set_ylim(0, min(yval)+max(yval))
		ax.bar(list(range(0, 10)), yval, 0.5, color='r')
		
	a=anim.FuncAnimation(fig, update, frames=None, repeat=False)
	plt.show()
			
		
	
if __name__=='__main__':
	test()

			
		
	

	
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
						
						
