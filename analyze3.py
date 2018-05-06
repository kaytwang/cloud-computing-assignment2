# note down the key information and turn them into a new json file

import json
import re
from textblob import TextBlob


def get_sentiment(text):

    t = TextBlob(text)

    s = t.sentiment

    return s.polarity, s.subjectivity


def get_called(text):

    called = re.findall(r'@', text)  # match all the @

    count = len(called)

    return count


def store(tweet):
    import json
    with open('projectdata.json', 'a+') as f:
        f.write(json.dumps(tweet))
        f.write('\n')


formaldata = 'cloud_data_doc_vic_line.json' # the last version of data from VIC

# practice dataset
# formaldata_temp = 'sample(1).json'
# formaldata_temp1 = 'tweettest.json'
# testdata = 'python2.json'


with open(formaldata, 'r') as data:  # might need to be redirected

    for line in data:

        # print line
        try:
            tweet = json.loads(line)
            # print tweet
            tweet_dic = {}  # a dic that consists of id, text ,etc information from twitter
            # global tweet_dic

            tweet_dic['tweetid'] = tweet['id']
            # print tweet_dic['tweetid']

            # tweet_dic['userid'] = tweet['user']['id']
            tweet_dic['userid'] = tweet['doc']['user']['id']
            # print tweet_dic['userid']

            # tweet_dic['text'] = tweet['text']
            tweet_dic['text'] = tweet['doc']['text']
            # print tweet_dic['text']

            # tweet_dic['coordinates'] = tweet['coordinates']  # demo
            tweet_dic['coordinates'] = tweet['value']['geometry']['coordinates']
            # print tweet_dic['coordinates']

            tweet_dic['followers'] = tweet['doc']['user']['followers_count']
            # print tweet_dic['followers']

            # tweet_dic['like'] = tweet['favorite_count']
            tweet_dic['like'] = tweet['doc']['favorite_count']
            # print tweet_dic['like']

            # tweet_dic['hashtag'] = len(tweet['entities']['hashtags'])
            tweet_dic['hashtag'] = len(tweet['doc']['entities']['hashtags'])
            # print tweet_dic['hashtag']

            tweet_dic['sentiment'] = get_sentiment(tweet_dic['text'])
            # print tweet_dic['sentiment']

            tweet_dic['number of @'] = get_called(tweet_dic['text'])
            # print tweet_dic['number of @']

            # print tweet_dic
            store(tweet_dic)

        except:

            continue





