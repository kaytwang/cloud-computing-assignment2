import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from config import Config

auth = tweepy.OAuthHandler(Config.consumer_key, Config.consumer_secret)
auth.set_access_token(Config.access_token, Config.access_token_secret)


class MyListener(StreamListener):
    def on_data(self, raw_data):
        try:
            with open('python.json', 'w') as f:
                f.write(raw_data)
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


twitter_stream = Stream(auth, MyListener())

# use filter to collect twitter information based on Australia field
while True:
    try:
        twitter_stream.filter(locations=[114.46, -38.28, 152.7, -11.79])
    except Exception as e:
        print e
    pass