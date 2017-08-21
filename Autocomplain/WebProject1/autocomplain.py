import time
import tweepy

def main(): 
    #auth = tweepy.OAuthHandler(key, secret)
    #auth.set_access_token(token, token_secret)
    #client = tweepy.API(auth)
    #client.update_status("#Python Rocks!")
    while True:
        print("Hello World")
        time.sleep(5)


if __name__ == '__main__':
    main()