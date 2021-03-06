# coding: utf-8

import pandas as pd
import tweepy #https://github.com/tweepy/tweepy
import csv, emoji, time
import pickle
import datetime

DJ_list = ['$MMM', '$AXP', '$AAPL', '$BA', '$CAT', '$CVX', '$CSCO', '$KO', '$DIS', '$DD',
           '$XOM', '$GE', '$GS', '$HD', '$IBM', '$INTC', '$JNJ', '$JPM', '$MCD', '$MRK',
           '$MSFT', '$NKE', '$PFE', '$PG', '$TRV', '$UTX', '$UNH', '$VZ', '$V', '$WMT']

def get_user_tweets(user_id, api):

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    # Initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(user_id = user_id, count=200, include_rts=0)

    #keep grabbing tweets until it reaches historical tweets on 2014-01-01 00:00:00
    while new_tweets != [] and new_tweets[-1].created_at >= datetime.datetime(2013,10,1,0,0,0):

        #update the id of the oldest tweet less one
        alltweets.extend(tw for tw in new_tweets if any(st in tw.text for st in DJ_list))
        oldest = new_tweets[-1].id - 1

        print "getting tweets before %s" % (new_tweets[-1].created_at)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(user_id = user_id, count=200, max_id=oldest)

        print "...%s related tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv
<<<<<<< HEAD
    outtweets = [[tweet.user.id_str, tweet.text.encode("unicode-escape"), tweet.retweet_count , tweet.created_at] for tweet in alltweets]
=======
    outtweets = [[tweet.user.id_str, tweet.text.encode("unicode-escape"), tweet.retweet_count, tweet.created_at] for tweet in alltweets]
>>>>>>> cc6f67fccd2d4d2fce217165ccbccb78855c0916

    return outtweets

def main():

    access_token = "Your access token"
    access_token_secret = "Your acess token secret"
    consumer_key = "Your consumer key"
    consumer_secret = "Your consumer secret"

    #Twitter only allows access to a users most recent 3240 tweets with this method
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    UID = pickle.load(open('/Users/wenying/Downloads/officialAccountID.pkl', 'rb'))
    missUser = []

    for user_id in UID:
        try:
            outtweets = get_user_tweets(user_id, api)
            with open('../data/tweets_{}.pkl'.format(user_id), 'wb') as f:
                pickle.dump(outtweets, f)
            print 'user {} finished \n'.format(user_id)
        except:
            print 'Miss user {}'.format(user_id)
            time.sleep(60*4)
            missUser.append(user_id)

    with open('../data/missUser.pkl', 'wb') as f:
        pickle.dump(missUser, f)
<<<<<<< HEAD

=======
        
>>>>>>> cc6f67fccd2d4d2fce217165ccbccb78855c0916
if __name__ == '__main__':
    main()






