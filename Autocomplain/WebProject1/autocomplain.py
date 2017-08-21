import time
import tweepy

def main(): 
    key =  'DTSG74qb7twxzGdgMA4GAH9bZ' 
    secret =  'kfpY2bzDZblf84tkgVXja6laSVW6KQVWXDOrh8b2CeOCrAg8kJ'
    token_secret = 'qMoWh6KOuzpEFjQraIfmBRRNDKeYGpCbmUooiGE1sqWDO'
    token = '899614983897657344-JUwDjKobLFwWHmZ8sRJEhlgpaMkx5Ag'
    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(token, token_secret)
    client = tweepy.API(auth)
    client.update_status("#Test Rocks!")

if __name__ == '__main__':
    main()