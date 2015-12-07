# coding: utf-8

import tweepy
import pandas as pd
import time
import pickle

access_token = "Your access token"
access_token_secret = "Your acess token secret"
consumer_key = "Your consumer key"
consumer_secret = "Your consumer secret"

def main():

    # Initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    officialAccountUID = []
    officialAccountName = pd.read_csv('/Users/wenying/Downloads/stock id.csv')

    for n in officialAccountName['Twitter Handler'][-300:]:
        try:
            UID = api.get_user(screen_name=n).id_str
            officialAccountUID.append(UID)
            print 'Find {}\'s UID'.format(n)
        except:
            print 'Rate Limit Error, ', 'miss user {}. Sleep for 15 mins'.format(n)
            time.sleep(15*60)
            print 'Retry {}'.format(n)
            UID = api.get_user(screen_name=n).id_str
            officialAccountUID.append(UID)

    with open('officialAccountID.pkl', 'wb') as f:
        pickle.dump(officialAccountUID, f)

if __name__ == '__main__':
    main()



