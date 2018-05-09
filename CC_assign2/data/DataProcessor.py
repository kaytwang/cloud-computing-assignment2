# note down the key information and turn them into a new json file

import json
import re
from textblob import TextBlob

class DataProcessor:

    def get_sentiment(self, text):
        t = TextBlob(text)
        s = t.sentiment

        return s.polarity, s.subjectivity

    def get_called(self, text):
        called = re.findall(r'@', text)  # match all the @
        count = len(called)

        return count

    def store(self, tweet):
        with open('projectdata.json', 'a+') as f:
            f.write(json.dumps(tweet))
            f.write('\n')

    def inVic(self, coordinates):
        if (((coordinates[0] <= 150.017) and (coordinates[0] >= 140.9617))
                and ((coordinates[1] <= -33.9806) and (coordinates[1] >= -39.1832))):
            return True
        else:
            return False

    def get_geo_twi_target_info_pro(self, raw):

        json_data = json.loads(raw)

        target_dic = {}

        target_dic['tweetid'] = json_data['id']
        target_dic['userid'] = json_data['doc']['user']['id']
        target_dic['text'] = json_data['doc']['text']
        target_dic['coordinates'] = json_data['value']['geometry']['coordinates']
        target_dic['followers'] = json_data['doc']['user']['followers_count']
        target_dic['like'] = json_data['doc']['favorite_count']
        target_dic['hashtag'] = len(json_data['doc']['entities']['hashtags'])
        target_dic['sentiment'] = self.get_sentiment(json_data['text'])
        target_dic['number of @'] = self.get_called(json_data['text'])

        return json.dumps(target_dic)

    def get_geo_twi_target_info(self, raw):

        json_data = json.loads(raw)

        try:
            if json_data['doc']['coordinates'] is None:
                return False
            if not self.inVic(json_data['doc']['coordinates']['coordinates']):
                return False
        except KeyError:
            return False

        target_dic = {}

        try:
            target_dic['tweetid'] = json_data['id_str']
            target_dic['userid'] = json_data['user']['id']
            target_dic['text'] = json_data['text']
            target_dic['coordinates'] = json_data['doc']['coordinates']
            target_dic['followers'] = json_data['user']['followers_count']
            target_dic['like'] = json_data['favorite_count']
            target_dic['hashtag'] = len(json_data['entities']['hashtags'])
            target_dic['sentiment'] = self.get_sentiment(json_data['text'])
            target_dic['number of @'] = self.get_called(json_data['text'])

        except KeyError:
            return False

        return json.dumps(target_dic)







