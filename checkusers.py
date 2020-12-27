import praw
import string
import net
import numpy

def getUsers():
	r = praw.Reddit( client_id = 'rrXYASXwqe9O2Q' , 
									 client_secret = 'SQu5rMreS9goYSrqr5C0g9T-qZk' , 
									 username = 'pupjaydetect' , password = 'sugarsugar' , 
									 user_agent = 'test1')

	sub_name = raw_input("What subreddit would you like to survey? : ")

	sub = r.subreddit(sub_name)

	hot = sub.hot(limit = 3) 
	print '\nCurrent top hot posts are: ' 
	userList = [[]]
	for x in hot :
		if(  not x.stickied) :
			print 'title : ' + x.title
			comments = x.comments.list()
			users = []
			for y in comments :
				users.append(y.author)
			userList.append(users)

	return userList	

#	for users in userList : 
#		for user in users :
#			print "overview for : " + user.name 
#			print "active sub ratio : " 
#			print net.activeSubs( user )
#			print "unique comment ratio : " 
#			print net.uniqueComments( user) 
#			print "average respose time : " 
#			print net.responseTime( user ) 
#			print "repetitive word ratio : "
#			print net.repetitveComments(user)
#			print 20*"---"

