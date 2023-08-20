from NudeNet import NudeClassifier
from flask import Flask, render_template, request, make_response, send_file
from PIL import Image
from io import BytesIO
from glob import glob
import pathlib, os, requests, json, mimetypes

NUDE_THRESHOLD = 0.8
model = NudeClassifier()
app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html", threshold=NUDE_THRESHOLD)


@app.route("/local")
def local():
    images = glob("images/*.png")
    images.extend(glob("images/*.jpg"))
    images.extend(glob("images/*.jpeg"))

    result = model.classify(images)
    return render_template("local.html", result=result, threshold=NUDE_THRESHOLD)


@app.route("/process", methods=["POST"])
def process():
    image_urls = request.get_json()

    imageFiles = []

    image_directory = "images"
    if not os.path.exists(image_directory):
        os.mkdir(image_directory)

    for image_url in image_urls:
        r = requests.get(image_url)
        i = Image.open(BytesIO(r.content))

        _, tail = os.path.split(image_url)
        extension = mimetypes.guess_extension(
            r.headers.get("content-type", "").split(";")[0]
        )
        imagePath = os.path.join(image_directory, tail.split("?")[0] + extension)
        i.save(imagePath)
        imageFiles.append(imagePath)

    results = model.classify(imageFiles)

    return make_response(json.dumps(results))


@app.route("/images/<name>", methods=["GET"])
def images(name=None):
    path = f"./images/{name}"
    if os.path.isfile(path):
        return send_file(path)

    return make_response("Image Not Found", 404)


if __name__ == "__main__":
    app.run()
