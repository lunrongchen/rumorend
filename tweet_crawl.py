import requests
import re
import time
import json
from bs4 import BeautifulSoup

def GetSingleTweetByUrl(_url):
    url = _url[:8] + "mobile." + _url[8:]
    tweet_html = requests.get(url)
    tweet_data = re.findall('<div class="dir-ltr" dir="ltr">(.*)\n<\/div>', tweet_html.text)
    tweet_url = re.findall('''<a href=['"](.*?)['\"].*?(?:<\/a|\/)>''', tweet_data[0])
    tweet_text = re.sub('''<a href=['"](.*?)['\"].*?(?:<\/a|\/)>''', '', tweet_data[0])
    result = {}
    result['text'] = tweet_text
    result['urls'] = []
    for url_it in tweet_url :
        try:
            r = requests.get(url_it)
            result['urls'].append(r.url)
        except:
            pass
    # result = json.dumps(result)
    return result

# start = time.time()
# url_test = "https://twitter.com/HillaryClinton/status/799043343275753472"
# print GetSingleTweetByUrl(url_test)
# end = time.time()
# print "--------------------"
# print end - start

def GetListUrlByGoogleKeywordSearch(_key_word):
    url_pre = "https://www.google.com/#safe=inactive&q="
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # url = url_pre + _key_word
    url = "https://www.google.com/#safe=inactive&q=trump"
    google_html = requests.get(url, headers=headers)
    # soup = BeautifulSoup(google_html.text, "html.parser")
    print google_html.text
    # tweet_data = re.findall('<cite class="(.*)">(.*)<\/cite>', google_html.text)
    # print tweet_data

if __name__ == '__main__':
    url_test = "https://twitter.com/HillaryClinton/status/796056175179599872"
    # url_test = "https://twitter.com/HillaryClinton/status/799043343275753472"
    print GetSingleTweetByUrl(url_test)
