import requests
import json
import tweepy # need to pip install tweepy
import twitter_info # still need this in the same directory, filled out

# SI 206 - W17 - HW5
# # COMMENT WITH:
# # Your section day/time: thursday 6-7PM
# Sara Ramaswamy
# # Any names of people you worked with on this assignment:

# ####### 500 points total ########

# # Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.
# ####### 500 points total ########

# # Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
# consumer_key = "" 
# consumer_secret = ""
# access_token = ""
# access_token_secret = ""
# ## Set up your authentication to Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way

## Write the rest of your code here!


# Fill these in in the twitter_info.py file

consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up library to grab stuff from twitter with your authentication, and return it in a JSON format 
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

phrase = input("Please type a phrase of choice: ") ## uses the python input function, satisfies hw requirement

# start out cache
CACHE_FNAME = "cached_data_socialmedia.json"
try:
	cache_file = open(CACHE_FNAME,'r')
	cache_contents = cache_file.read()
	CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}


def get_tweets_from_user(phrase):
	unique_identifier = "twitter_{}".format(phrase) # seestring formatting chapter
	# see if that username+twitter is in the cache diction!
	if unique_identifier in CACHE_DICTION: # if it is...
		print('using cached data for', phrase)
		twitter_results = CACHE_DICTION[unique_identifier] # grab the data from the cache!
	else:
		print('getting data from internet for', phrase)
		twitter_results = api.user_timeline(phrase) # get it from the internet
		# but also, save in the dictionary to cache it!
		CACHE_DICTION[unique_identifier] = twitter_results # add it to the dictionary -- new key-val pair
		# and then write the whole cache dictionary, now with new info added, to the file, so it'll be there even after your program closes!
		f = open(CACHE_FNAME,'w') # open the cache file for writing
		f.write(json.dumps(CACHE_DICTION)) # make the whole dictionary holding data and unique identifiers into a json-formatted string, and write that wholllle string to a file so you'll have it next time!
		f.close()

	# now no matter what, you have what you need in the twitter_results variable still, go back to what we were doing!
	tweet_texts = [] # collect 'em all!
	created_at = []
	tweet_count = 0
	for tweet in twitter_results:
		if tweet_count < 3:
			print("TEXT: ", tweet["text"])
			tweet_texts.append(tweet["text"])
			print("CREATED AT: ", tweet["created_at"])
			created_at.append(tweet["created_at"])
			print("\n")
			tweet_count = tweet_count + 1

three_tweets = get_tweets_from_user(phrase) # try with your own username, too! or other umich usernames!
print(three_tweets)

	# for tweet in twitter_results:
	# 	tweet_texts.append(tweet["text"])
	# 	created_at.append(tweet["created_at"])
	
# print(three_tweets("umich"))

# Let's take a look at the output in a nice way...


# for t in three_tweets:
# 	print("TEXT:", t)
# 	print("\n")