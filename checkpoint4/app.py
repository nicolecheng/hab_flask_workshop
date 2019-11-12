from flask import Flask, render_template, request
# https://docs.clarifai.com/api-guide/train#train
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

key = 'd8c6adff128c41d8a95a375cea3357dc'
app = ClarifaiApp(api_key=key)

def get_photo_tags(link):
    model = app.models.get('general-v1.3')
    image = ClImage(url=link)
    u = model.predict([image])
    concepts = u['outputs'][0]['data']['concepts']
    tags = []
    for tag in concepts:
        tags.append(tag['name'])
    return tags

my_app = Flask(__name__)

@my_app.route("/", methods=["GET"])
def index():
    img_url = "https://thumbs.dreamstime.com/z/perfect-green-appl-apple-isolated-white-background-48734377.jpg"
    return render_template('index.html', image=img_url)

if __name__ == '__main__':
    my_app.run(debug=True)