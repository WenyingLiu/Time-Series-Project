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
    missUsername = []
    officialAccountName = pd.read_csv('/Users/wenying/Downloads/stock id.csv')

    for n in officialAccountName['Twitter Handler'][-300:]:
        try:
            UID = api.get_user(screen_name=n).id_str
            nFollowers = api.get_user(screen_name=n).followers_count
            officialAccountUID.append((UID, nFollowers))
            print 'Find {}\'s UID'.format(n)
        except:
            print 'Rate Limit Error, ', 'miss user {}. Sleep for 15 mins'.format(n)
            time.sleep(15*60)
            missUsername.append(n)
            #print 'Retry {}'.format(n)
            #UID = api.get_user(screen_name=n).id_str
            #nFollowers = api.get_user(screen_name=n).followers_count
            #officialAccountUID.append((UID, nFollowers))

    with open('officialAccountID.pkl', 'wb') as f:
        pickle.dump(officialAccountUID, f)
        
    with open('missUsername.pkl', 'wb') as f:
        pickle.dump(missUsername, f)
        
        
if __name__ == '__main__':
    main()



