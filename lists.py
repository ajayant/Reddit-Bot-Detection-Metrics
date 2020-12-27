import net 
import csv

red = praw.Reddit()

def getrealList( ):
	file1= open( "humans.text" ,"r" )
	realList = []
	for line in file1 :
		realList.append( createUser) 
	return realList


def gettbotList( ):
	file1 = open( "bots.txt" , "r") 
	botList = []
	for line in file1 :
		botList.append( createUser(line)) 
	return botList

def createUser( username ):
	return red.redditor(username)

