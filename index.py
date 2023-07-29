from NudeNet import NudeClassifier
from flask import Flask, render_template, request, make_response, send_file
from PIL import Image
from io import BytesIO
import os, requests, json, mimetypes

model = NudeClassifier()
app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    image_urls = request.get_json()

    imageFiles = []

    for image_url in image_urls:
        r = requests.get(image_url)
        i = Image.open(BytesIO(r.content))

        _, tail = os.path.split(image_url)
        extension = mimetypes.guess_extension(
            r.headers.get("content-type", "").split(";")[0]
        )
        imagePath = "images/" + tail.split("?")[0] + extension
        i.save(imagePath)
        imageFiles.append(imagePath)

    results = model.classify(imageFiles)

    return make_response(json.dumps(results))


@app.route("/images/<name>", methods=["GET"])
def images(name=None):
    path = f"./images/{name}"
    print(os.path.isfile(path), path)
    if os.path.isfile(path):
        return send_file(path)

    return make_response("Image Not Found", 404)


if __name__ == "__main__":
    app.run()
