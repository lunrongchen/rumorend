import requests
import re
import time
from time import sleep
import json
from bs4 import BeautifulSoup


def GetSingleTweetByUrl(_url):
    url = _url[:8] + "mobile." + _url[8:]
    tweet_user = _url.split('/')[3]
    tweet_html = requests.get(url)
    sleep(0.2)
    tweet_data = re.findall('<div class="dir-ltr" dir="ltr">(.*)\n<\/div>', tweet_html.text)
    tweet_url = re.findall('''<a href=['"](.*?)['\"].*?(?:<\/a|\/)>''', tweet_data[0])
    tweet_text = re.sub('''<a href=['"](.*?)['\"].*?(?:<\/a|\/)>''', '', tweet_data[0])
    result = {}
    result['user'] = tweet_user
    result['text'] = tweet_text
    result['urls'] = []
    for url_it in tweet_url:
        try:
            r = requests.get(url_it)
            sleep(0.1)
            result['urls'].append(r.url)
        except:
            pass
    return result


def GetUserScoreById(_user):
    identity_url_pre = "http://api.klout.com/v2/identity.json/twitter?screenName="
    identity_url_suf = "&key=judkzmdxkjmy3dvngcx9ateq"
    identity_url_request = identity_url_pre + _user + identity_url_suf
    identity_info_text = requests.get(identity_url_request).text
    sleep(0.2)
    identity_info_json = json.loads(identity_info_text)
    score_url_pre = "http://api.klout.com/v2/user.json/"
    score_url_suf = "/score?key=6ubcypzb7x9ruqgpmc2s8rds"
    score_url_request = score_url_pre + identity_info_json['id'] + score_url_suf
    score_info_text = requests.get(score_url_request).text
    sleep(0.2)
    score_info_json = json.loads(score_info_text)
    return score_info_json['score']


def GetListUrlByGoogleKeywordSearch(_key_word):
    url_pre = "https://www.google.com/search?q="
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    exclude_site = " -site:twitter.com -site:www.twitter.com"
    url = url_pre + _key_word + exclude_site + "&num=20"
    google_html = requests.get(url, headers=headers)
    google_urls = re.findall('''<a href=['"](.*?)['\"].*?(?:<\/a|\/)>''', google_html.text)
    result = set()
    for google_url in google_urls:
    	domain_splits = google_url.split('/')
    	if domain_splits[0] == 'https:' or domain_splits[0] == 'http:':
    		result.add(domain_splits[2])
    try:
    	result.remove("www.google.com")
        result.remove("support.google.com")
    except:
    	pass
    return result


if __name__ == '__main__':
    # url_test = "https://twitter.com/HillaryClinton/status/796056175179599872"
    # url_test = "https://twitter.com/HillaryClinton/status/799043343275753472"
    # print GetSingleTweetByUrl(url_test)
    # GetUserScoreById("HillaryClinton")
    print GetListUrlByGoogleKeywordSearch("trump")


