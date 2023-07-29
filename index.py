from NudeNet import NudeClassifier
from flask import Flask, render_template, request, make_response
import requests, json

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    images = request.get_json()
    print(images)

    results = [{"url": x, "adult": True} for x in images]

    return make_response(json.dumps(results))


if __name__ == "__main__":
    model = NudeClassifier()
    app.run()
