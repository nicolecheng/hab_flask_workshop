from flask import Flask, render_template, request, redirect
import json, urllib

# clarifai stuff
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

key = 'd8c6adff128c41d8a95a375cea3357dc'
app = ClarifaiApp(api_key=key)

# makes sure there's an http url type
def clean_link(link):
    if link.find("http") == -1:
        return "http://"+link
    return link

# CLARIFAI API TOOLS


# given a link to an image, returns a list of tags
def get_photo_tags(link):
    link = clean_link(link)
    model = app.models.get('general-v1.3')
    image = ClImage(url=link)
    u = model.predict([image])
    concepts = u['outputs'][0]['data']['concepts']
    tags = []
    for tag in concepts:
        tags.append(tag['name'])
    return tags
    

apple = "https://thumbs.dreamstime.com/z/perfect-green-appl-apple-isolated-" + \
"white-background-48734377.jpg"


my_app = Flask(__name__)

@my_app.route("/")
def index(image=None):
    print("sent an apple photo...", get_photo_tags(apple))
    return render_template('index.html', image=None)



@my_app.route("/upload", methods=["GET", "POST"])
def upload():
    img_url = request.form['img'] 
    img_data = {"url": img_url, "description": get_photo_tags(img_url)}
    return render_template('index.html', image=img_data)




if __name__ == '__main__':
    my_app.run(debug=True)
