import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from config import Config
auth = tweepy.OAuthHandler(Config.consumer_key, Config.consumer_secret)
auth.set_access_token(Config.access_token, Config.access_token_secret)

class myListener(StreamListener):
    def on_data(self, raw_data):
        try:
            with open('python.json', 'w') as f:
                f.write(raw_data)
                return True
        except BaseException as e:
            print("Error on_data:%s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

    def on_timeout(self):
        print("ERROR: Timeout...")
        return True  # Don't kill the stream


twitter_stream = Stream(auth, myListener())

#use filter to collect twitter information
twitter_stream.filter(track=["melbourne"])