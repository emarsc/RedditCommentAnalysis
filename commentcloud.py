import commentparse as parse
import commentcollect as collect
import commentanalysis as analysis
import sys




def display_cloud(word_dict, words, index=1, positive=True, num_words=None): 
	import matplotlib.pyplot as plt
	from wordcloud import WordCloud
	text=[]
	if num_words is None:
		num_words=len(words)
	if positive:
		lower=len(words)-num_words
		upper=len(words)
		sign=1		
	else:
		lower=0
		upper=num_words
		sign=-1
	for i in range(lower, upper):
		magnitude=sign*word_dict[words[i]][index]
		if magnitude>0:
			text.extend([words[i]]*word_dict[words[i]][index])
		#print(words[i])
	text=" ".join(text)
	wordcloud=WordCloud(collocations=False).generate(text)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()

	print("Printing the lowest 10 words followed by the highest scored 10 words.  (score=total comment score)")
	print("<WORD:  SCORE>")
	for i in range(0, 10):
		print(words[i]+":  "+str(word_dict[words[i]][index]))
	print(".....:  .\n.....:  .")
	for i in range(len(words)-10, len(words)):
		print(words[i]+":  "+str(word_dict[words[i]][index]))

	

if __name__=='__main__':
	if len(sys.argv)<2:
		print("Must specify subreddit name")
		sys.exit()
	subname=sys.argv[1]
	index=1
	if len(sys.argv)>2:
		index=int(sys.argv[2])

	submissions=collect.get_hot(subname)
	subarray=[]
	for sub in submissions:
		subarray.append(sub)
	i=1
	print("Input the index corresponding to the post you would like to model")
	print("<index>: <post title>")
	for sub in subarray:
		print(str(i)+": "+sub.title)
		i+=1
	choice=int(input("..."))-1
	print("collecting comments...")
	commentdata=collect.collect_submission(subarray[choice])
	headline=commentdata['post']
	print("Processing comments...")
	submission, words=parse.process_submission(commentdata)
	print("Sorting data...")
	word_dict, words=analysis.comment_word_dict(words, [submission], normal=False)
	words=analysis.sort_words(words, word_dict, index=index)
	#print(str(words))
	print("Creating cloud...")
	print("Submission Title: "+str(headline))
	display_cloud(word_dict, words, index=index)
	
	
