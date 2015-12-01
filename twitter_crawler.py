from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json

# Variables that contains the user credentials to access Twitter API
access_token = "1604502054-DF0gfKMskzRDEdywKxoMlaEfOJnQhxy2DkdgfFM"
access_token_secret = "FCoSIVkT9Ilcw2svpfxXtopLTXRIb0feUCh9dAPvPr9X5"
consumer_key = "qZqEK9TSVCC9ZZVUlhTRT01Cz"
consumer_secret = "r12WukMn1Znn1sDUNfZd8oIU41gAsaxVRvEKV4ykfdBuOqgi2C"

DJ_list = ['$MMM', '$AXP', '$AAPL', '$BA', '$CAT', '$CVX', '$CSCO', '$KO', '$DIS', '$DD',
               '$XOM', '$GE', '$GS', '$HD', '$IBM', '$INTC', '$JNJ', '$JPM', '$MCD', '$MRK',
                          '$MSFT', '$NKE', '$PFE', '$PG', '$TRV', '$UTX', '$UNH', '$VZ', '$V', '$WMT']


#Adjust the basic listener to only print out certain tweets.
class StdOutListener(StreamListener):

    def on_data(self, data):

        jsonData = json.loads(data)
        # Filter out retweets.
        if not jsonData['retweeted'] and 'RT @' not in jsonData['text']:
            print jsonData['id_str'], jsonData['text'].strip(), datetime.strptime(jsonData['created_at'], '%a %b %d %H:%M:%S +0000 %Y'), '\n'

        return True

    def on_error(self, status):
        print status

def main():

    # Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(languages=['en'], track=DJ_list)


if __name__ == '__main__':
    main()