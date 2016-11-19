import requests
import re

def getResultByWOT(_url):
    url_pre = "http://api.mywot.com/0.4/public_link_json2?hosts="
    url_suf = "/&callback=process&key=9af2a6793e479dacfbc52e93fffd5ae39c6b2a5f"
    url_request = url_pre +  _url + url_suf
    WOT_result_jsonp = requests.get(url_request)
    WOT_result_json = re.sub(r'([a-zA-Z_0-9\.]*\()|(\);?$)','',WOT_result_jsonp.text)
    print WOT_result_json

getResultByWOT("https://www.hillaryclinton.com/")