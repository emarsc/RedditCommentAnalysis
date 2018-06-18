import utility
from utility import CommentStream

stream=CommentStream()


def get_parsed_data():
	print("getting data")
	stream.update_comments()
	print('comments updated')
	comments=[]
	submissions={}
	subreddits={}
	for comment in stream.comments:
		#subid=comment.submission.id
		subtitle=comment.link_title
		subreddit=str(comment.subreddit)
		submissions[subtitle]=0
		subreddits[subreddit]=0
		tokens=utility.comment_tokens(comment.body)
		comments.append((list(tokens), subreddit, subtitle))
	return subreddits, submissions, comments
	
	
	

def longest_common_subsequence(pat1, pat2):
	seq=[]
	#print(str(pat1))
	#print(str(pat2))
	for i in range(0, len(pat1)+1):
		ar=[]
		for i in range(0, len(pat2)+1):
			ar.append([])
		seq.append(ar)
	flag=False	
	for i in range(1, len(pat1)+1):
		flag=False
		temp=seq[i-1][0]
		for j in range(1, len(pat2)+1):
			if(pat1[i-1]==pat2[j-1]):
				temp=seq[i-1][j-1]+[pat1[i-1]]
				flag=True
			if(flag and len(temp)>len(seq[i-1][j])):
				seq[i][j]=temp
			else:
				seq[i][j]=seq[i-1][j]
	return seq[len(pat1)][len(pat2)]
	
def score_sequence(seq):
	subredditScores, submissionScores, comments=get_parsed_data()
	print("got data")
	longestSequence=""
	for comment in comments:
		longest=longest_common_subsequence(seq, comment[0])
		lcsLength=len(longest)
		#print(str(lcsLength))
		if lcsLength>len(longestSequence):
			longestSequence=longest
		subredditScores[comment[1]]+=lcsLength
		submissionScores[comment[2]]+=lcsLength
	topSubreddits=utility.find_top_keys(subredditScores)
	topSubmissions=utility.find_top_keys(submissionScores)
	return longestSequence, topSubmissions, topSubreddits, subredditScores, submissionScores
	
	
if __name__=="__main__":
	seq=utility.comment_tokens(input("Input sequence to analyze."))
	print(seq)
	while seq!="exit":
		longestSequence, topSubmissions, topSubreddits, subredditScores, submissionScores=score_sequence(seq)
		print("Longest sub-sequence: "+str(longestSequence))
		print("Top subreddits: ")
		for i in range(0, 10):
			print(topSubreddits[i]+" : "+str(subredditScores[topSubreddits[i]]))
		print("Top submissions:")
		for i in range(0, 10):
			print(topSubmissions[i]+" : "+str(submissionScores[topSubmissions[i]]))
		seq=utility.comment_tokens(input("Input sequence to analyze"))
		print(seq)
	
	
		
	