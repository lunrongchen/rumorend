import requests
import re
import time

def GetSingleTweetByUrl(_url):
	url = _url[:8] + "mobile." + _url[8:]
	tweet_html = requests.get(url)
	tweet_data = re.findall('<div class="dir-ltr" dir="ltr">(.*)\n<\/div>', tweet_html.text)
	tweet_data = re.sub('''<a href=['"](.*?)['\"].*?(?:<\/a|\/)>''', '', tweet_data[0])
	return tweet_data

url_test = "https://twitter.com/HillaryClinton/status/799043343275753472"
print GetSingleTweetByUrl(url_test)
