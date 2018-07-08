import oauth2 as oauth
import json
import cgitb
cgitb.enable()

CONSUMER_KEY = "25Nn7SSSV3N2Mlin0160ZzY1y"
CONSUMER_SECRET = "RFOvzHAcB6wxXD9dwwo3VP5ApgkcUvLs55HNmnJ5hyfbskKKey"
ACCESS_KEY = "3278986909-eObdrXEmG2bhUrqaHrFXZ21L2aO5DcYWRHej93z"
ACCESS_SECRET = "PR8bkKT0FLlN6RewBrSM8PT3rmwML41eN8wpVNnvRwM10"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

base = "https://api.twitter.com/1.1/tweets/search/"

method = "fullarchive/"

environment = "cryptoChecks.json?"

keyword = "hi"
fromDate = "201807010000"
toDate = "201807070000"

variables = "q="+keyword+"&fromDate="+fromDate+"&toDate="+toDate

query = base + method + environment + variables

#response, data = client.request(query)


#if(response):
#    tweets = json.loads(response.decode('utf-8'))
#    for tweet in tweets:
#        print (tweet)
#else:
print (query)
