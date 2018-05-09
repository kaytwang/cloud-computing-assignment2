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


with open(formaldata, 'r') as data:  # might need to be redirected

    for line in data:
        try:
            tweet = json.loads(line)

            tweet_dic = {}  # a dic that consists of id, text ,etc information from twitte

            tweet_dic['tweetid'] = tweet['id']

            tweet_dic['userid'] = tweet['doc']['user']['id']

            tweet_dic['text'] = tweet['doc']['text']
       
            tweet_dic['coordinates'] = tweet['value']['geometry']['coordinates']

            tweet_dic['followers'] = tweet['doc']['user']['followers_count']

            tweet_dic['like'] = tweet['doc']['favorite_count']

            tweet_dic['hashtag'] = len(tweet['doc']['entities']['hashtags'])

            tweet_dic['sentiment'] = get_sentiment(tweet_dic['text'])

            tweet_dic['number of @'] = get_called(tweet_dic['text'])

            store(tweet_dic)

        except:

            continue





