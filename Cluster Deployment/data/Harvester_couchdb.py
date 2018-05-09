import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from Config import Config

from Connector import Connector
from DataProcessor import DataProcessor

class MyListener(StreamListener):

    def __init__(self):
        self.dp = DataProcessor()
        self.conf = Config()
        self.auth = tweepy.OAuthHandler(self.conf.consumer_key, self.conf.consumer_secret)
        self.auth.set_access_token(self.conf.access_token, self.conf.access_token_secret)
        self.conn = Connector()

    def on_data(self, raw_data):
        try:
            self.conn.insert_raw_twitter(raw_data, self.conn.twitterdb_demo_pub)

            target_info = self.dp.get_geo_twi_target_info(raw_data)

            self.conn.insert_raw_twitter_result(target_info, self.conn.twitterdb_demo_results_pub)

            if target_info:
                self.conn.insert_raw_twitter_result(target_info, self.conn.twitterdb_demo_results_pub)

            return True

        except BaseException as e:
            print("Error on_data:%s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print("ERROR: Rate limit reached")
        print(status_code)
        return True

    def on_timeout(self):
        print("ERROR: Timeout...")
        return True  # Don't kill the stream


if __name__ == "__main__":

    myListener = MyListener()

    twitter_stream = Stream(myListener.auth, MyListener())

    # use filter to collect twitter information based on Victoria
    while True:
        try:
            twitter_stream.filter(locations=[140.9617, -39.1832, 150.017, -33.9806])
        except Exception as e:
            print(e)
            pass



