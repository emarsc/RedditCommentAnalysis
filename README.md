# RedditCommentAnalysis
Displays word clouds of currently hot submissions' comment replies on reddit using user specified subreddit and post title from a displayed list. Testing.

(This is intended to be a small testing application of a larger reddit comment analysis program. This application is not yet complete.)

Python3



Dependencies: WordCloud, matplotlib

To run program type: python3 commentcloud.py <subreddit name> <index>
'index is an optional parameter denoting what parameter of the comment data will be modeled. 
index=0 will model the sheer frequency of the words in the comments.
index=1 will model the total score (upvotes/downvotes) of the words in the comments
index defaults to 1 to model popularity

A list of submission titles will then be displayed and the user then specifies a submission to model with the given index displayed next to the submission title.
A word cloud will then be displayed.

It takes a substantial amount of time to collect comments on large submissions.

Have fun.
