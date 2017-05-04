
from pprint import pprint
from random import choice
import tweepy
import georgeWBot


# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'tpfrsZPgaoydKIPUX81HouFHg'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'mtYT0sN1N0iNWbjmOre5RrVZM2nWLC2itJDcfpWIyFe0SM5BFO'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '778330535789670400-QnS4eyd5M9TAVsR16uLKthM9MVndAWW'  # keep the quotes, replace this with your access token
ACCESS_SECRET = 'QCxlyxY4oOhUdQNGuXvGUYnvPghYelUCRPAyga2cVWOkt'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



#takes the user's first 200 tweets and puts them in a list
def mineTweets(screenName):
    minedTweets = []
    newTweets = api.user_timeline(screen_name=screenName,count=200)
    minedTweets.extend(newTweets)
    #lastTweet = minedTweets[-1].id
    #TODO

    return True


#Create a tweet and update status
george = georgeWBot.GeorgeWBot()
georgesText = george.makeTweetText()
georgesTweet = george.createTweet(georgesText)
api.update_status(georgesTweet)




"""
public_tweets = api.home_timeline(count=1) #list with one tweet
for tweet in public_tweets:
    #print(tweet)
    #print(tweet.user.screen_name)
    #print(tweet.text + "\n")

    tweetString = tweet.text
    otherUser = tweet.user.screen_name

    tweetList = tweetString.split()
    if "@GeorgeWBot" in tweetList and otherUser == "GeorgeWBot":
        print("you were tweeted at by " + otherUser)
        #theirTweets = mineTweets(otherUser)

"""



#Streaming API
"""
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.user.id)
        return status.user.id



    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@GeorgeWBot'], async=True)
"""