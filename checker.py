import json
import re
import requests
from time import sleep
from random import randint

def getResultByWOT(_url):
    fail_cnt = 0
    while True:
        try:
            url_pre = "http://api.mywot.com/0.4/public_link_json2?hosts="
            url_suf = ["/&callback=process&key=9af2a6793e479dacfbc52e93fffd5ae39c6b2a5f", "/&callback=process&key=48423d8d2f761abebf91f07885dc0eb9ece8c0a7"]
            url_request = url_pre +  _url + url_suf[randint(0,1)]
            WOT_result_jsonp = requests.get(url_request)
            WOT_result_json = re.sub(r'([a-zA-Z_0-9\.]*\()|(\);?$)', '', WOT_result_jsonp.text)
            # print WOT_result_json
            return json.loads(WOT_result_json)
        except:
            fail_cnt += 1
            if fail_cnt >= 2:
                return None

def getSafeScore(_url):
    # print _url
    wot_result_json = getResultByWOT(_url)
    if wot_result_json is None:
        return None
    wot_result_json = wot_result_json.values()[0]
    total = 0
    n = 0
    if "0" in wot_result_json:
        total += wot_result_json["0"][0]
        n += 1
    if "4" in wot_result_json:
        total += wot_result_json["4"][0]
        n += 1
    if n == 0:
        return None
    return total / n

def main():
    print getSafeScore("www.example.com")
    print getSafeScore("www.google.com")
    print getSafeScore("www.baidu.com")

if __name__ == '__main__':
    main()
