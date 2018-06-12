import tweepy
from tweepy import OAuthHandler

consumer_key = "25Nn7SSSV3N2Mlin0160ZzY1y"
consumer_secret = "RFOvzHAcB6wxXD9dwwo3VP5ApgkcUvLs55HNmnJ5hyfbskKKey"
access_token = "3278986909-eObdrXEmG2bhUrqaHrFXZ21L2aO5DcYWRHej93z"
access_token_secret = "PR8bkKT0FLlN6RewBrSM8PT3rmwML41eN8wpVNnvRwM10"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# The search term you want to find
query = "init coin offering"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print (tweet.user.screen_name,"Tweeted:",tweet.text)

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='{username}',
  password='{password}',
  version='2018-03-16')