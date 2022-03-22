import tweepy

#get all the relevant info from the user
consumer_key = input("\nPlease introduce your consumer key: ")
consumer_secret = input("\nPlease introduce your consumer secret: ")
access_token = input("\nPlease introduce your acess token: ")
access_token_secret = input("\nPlease introduce your access token secret: ")

#authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print("\nLaunching api...")

#launch api
api = tweepy.API(auth)

#get the tweet from the user
tweet = "Good Morning!"

#tweet
print("\nTweeting...")
status = api.update_status(tweet)

print("\n\nTwitter status updated!")
