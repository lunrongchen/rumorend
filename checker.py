import json
import re
import requests

def getResultByWOT(_url):
    url_pre = "http://api.mywot.com/0.4/public_link_json2?hosts="
    url_suf = "/&callback=process&key=9af2a6793e479dacfbc52e93fffd5ae39c6b2a5f"
    url_request = url_pre +  _url + url_suf
    WOT_result_jsonp = requests.get(url_request)
    WOT_result_json = re.sub(r'([a-zA-Z_0-9\.]*\()|(\);?$)', '', WOT_result_jsonp.text)
    return json.loads(WOT_result_json)

def getSafeScore(_url):
    wot_result_json = getResultByWOT(_url).values()[0]
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
