import random

from flask import Flask, request, jsonify
from tweet_crawl import GetSingleTweetByUrl
from checker import getSafeScore

context = ("cert/server.crt", "cert/server.key")
app = Flask("rumorend")

@app.route("/rumor_detect_fake", methods=["POST"])
def rumor_detect_fake():
    query = request.get_json() or request.form
    if "url" not in query:
        return jsonify(None)
    result = random.randint(0, 100)
    return jsonify(result)

@app.route("/example")
def example():
    return app.send_static_file("example.html")

@app.route("/rumor_detect", methods=["POST"])
def rumor_detect():
    query = request.get_json() or request.form
    if "url" not in query:
        return jsonify(None)
    url = query["url"]
    tweet_info = GetSingleTweetByUrl(url)
    urls = tweet_info["urls"]
    scores = [getSafeScore(url) for url in urls if "twitter.com" not in url]
    if len(scores) == 0:
        return jsonify(80 + random.randint(5))
    return jsonify(sum(scores) / len(scores))

def main():
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=context)

if __name__ == '__main__':
    main()
