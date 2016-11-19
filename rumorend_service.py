import random

from flask import Flask, request, jsonify

app = Flask("rumorend")

@app.route("/rumor_detect_fake", methods=["POST"])
def rumor_detect_fake():
    json_query = request.get_json()
    if "url" not in json_query:
        return jsonify(None)
    result = random.randint(0, 100)
    return jsonify(result)
