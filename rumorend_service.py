import random

from flask import Flask, request, jsonify

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
