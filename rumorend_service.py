import random

from flask import Flask, request, jsonify
from tweet_crawl import GetSingleTweetByUrl

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
    tweet = GetSingleTweetByUrl(url)

def main():
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=context)

if __name__ == '__main__':
    main()
    