import json
import os


def comment_word_dict(words, posts, normal=True):
	word_dict={}
	for word in words:
		word_dict[word]=[0, 0]
	for p in posts:
		for c in p['comments']:
			comment=c[0].split(" ")
			score=int(c[1])
			for word in comment:
				word_dict[word][0]+=1
			comment=set(comment)
			for word in comment:
				word_dict[word][1]+=score
	if normal:
		#normalizing the scores of words with respect to their frequency
		for word in words:
			word_dict[word][1]=word_dict[word][1]/word_dict[word][0]
	return word_dict, words

def sort_words(words, word_dict, index=1):
	#quicksort.  index denotes the dictionary array value of interest. 
	#default index=1 implies sorting based on word(comment) score. index=0 implies sorting based on word frequency 
	if len(words)<=1:
		return words
	less=[]
	equal=[]
	more=[]
	pivot=word_dict[words[len(words)//2]][index]
	for word in words:
		if(word_dict[word][index]>pivot):
			more.append(word)
		elif(word_dict[word][index]<pivot):
			less.append(word)
		else:
			equal.append(word)
	less=sort_words(less, word_dict, index=index)
	more=sort_words(more, word_dict, index=index)
	return less+equal+more

if __name__=='__main__':
	with open('words.json', 'r') as file:
		words=json.load(file)
	file.close()
	posts=[]
	files=os.listdir('processed/')
	for fname in files:
		with open('processed/'+fname, 'r') as file:
				posts.extend(json.load(file))
		file.close()
	word_dict, words=comment_word_dict(words, posts, normal=True)
	#print(str(word_dict))
	words=sort_words(words, word_dict)
	print("Printing the lowest 10 words followed by the highest scored 10 words.  (score=total 	comment score)")
	print("<WORD:  SCORE>")
	for i in range(0, 10):
		print(words[i]+":  "+str(word_dict[words[i]][1]))
	print(".....:  .\n.....:  .")
	for i in range(len(words)-10, len(words)):
		print(words[i]+":  "+str(word_dict[words[i]][1]))
 
