import time
from datetime import datetime
import tweepy
from autocomplain import tweepy

def main():
	while(True):
		dateDiff = datetime.now() - datetime(2017, 8, 1) 
		days = str(int(dateDiff.total_seconds() / 86400))
		hours = str(int(dateDiff.total_seconds() / 3600))
		minutes = str(int(dateDiff.total_seconds() / 60))
		seconds = str(int(dateDiff.total_seconds()))

		tweet = "@UPSHelp @UPS @UPS_News @pimoroni TrNo 1Z8A1E460491377435 " + days + " Days " + hours + " Hours " + minutes + " Minutes " + seconds + " Seconds Still Waiting !!! #CustomerService"
		time.sleep(10)
		
		key =  'DTSG74qb7twxzGdgMA4GAH9bZ' 
		secret =  'kfpY2bzDZblf84tkgVXja6laSVW6KQVWXDOrh8b2CeOCrAg8kJ'
		token_secret = 'qMoWh6KOuzpEFjQraIfmBRRNDKeYGpCbmUooiGE1sqWDO'
		token = '899614983897657344-JUwDjKobLFwWHmZ8sRJEhlgpaMkx5Ag'
		auth = tweepy.OAuthHandler(key, secret)
		auth.set_access_token(token, token_secret)
		client = tweepy.API(auth)
		client.update_status(tweet)

if __name__ == '__main__':
    main()