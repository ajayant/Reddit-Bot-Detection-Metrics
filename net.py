import numpy
import praw 
import checkusers

def NN( m1, w1 , m2 , w2 , m3 , w3 , b) :
	z = (m1*w1) + (m2*w2) + (m3*w3) + b
	sigmoid(z)

def sigmoid( x ) : 
# standard activation function
	return 1/(1 + numpy.exp(-x))

def uniqueComments( user ) :
# unique comments by a given user returns a percent
# many unique comments indicate that its probably not a bot
	allcom = [ x for x in user.comments.new(limit = 30) ] 
	uniqueList = []
	for comment in allcom :
		if comment.body not in uniqueList : 
			uniqueList.append(comment.body)

	return float(len( uniqueList )) / float(len(allcom))
	


def repetitveComments( user ) :
# check if there are certain words that are used in every comment
# DEBUG THIS NO WAY IT WORKS LMAO 	
	allcom = [ x for x in user.comments.new(limit = 2) ]
	count = 0 
	totalwords = 0
	repeatwords = 0
 
	for comment in allcom : 
		words = comment.body.split(" ")
		for commentCheck in allcom  : 
			if( comment.body != commentCheck.body) : 
				checker =  commentCheck.body.split(" ")
				for word in checker : 
					if word in words : 
						repeatwords = repeatwords + 1
		totalwords += len(words)
	
	repeatwords = repeatwords/2
	return ( float(repeatwords) / float(totalwords))

def responseTime( user ) : 
# bots usually have very low response times so check its response times
	allcom = [ x for x in user.comments.new( limit = 6)]
	timelist = []
	timesum = 0
	for comment in allcom :
		timelist.append(comment.created_utc-comment.parent().created_utc)
		timesum = timesum + comment.created_utc-comment.parent().created_utc

	return float(timesum) / float(len(timelist))


def activeSubs( user ) : 
# bots normally use many subreddits while real users will only use a few
	allcom = [ x for x in user.comments.new( limit = 50)] 
	allsubs = []
	for comment in allcom :
		if comment.subreddit not in allsubs:
			allsubs.append(comment.subreddit)

	return float(len(allcom)) / float(len(allsubs))


