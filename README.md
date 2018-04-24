# RedditCommentAnalysis

Dependencies: python3, praw (python reddit api wrapper), matplotlib, nltk

Displays a changing chart showing the frequency of words for a specified set of subreddits.

'subreddits.txt' should contain a space-seperated list of subreddits for the script to consider. 

To run, 'python3 wordChartAnimation.py' <numComments> <commentBufferSize>

Optional arguments: 
	numComments=the total number of comments to consider in a single chart.  Default=1000
	commentBufferSize=the number of comments to alternate for one animation pass

To exit, close the matplotlib animation.
