from flask import Flask, render_template, request
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

my_app = Flask(__name__)
key = 'd8c6adff128c41d8a95a375cea3357dc'
app = ClarifaiApp(api_key=key)

### CLARIFAI API TOOLS ###
# Given a link to an image, returns a list of tags
def get_photo_tags(link):
    model = app.models.get('general-v1.3')
    image = ClImage(url=link)
    u = model.predict([image])
    concepts = u['outputs'][0]['data']['concepts']
    tags = []
    for tag in concepts:
        tags.append(tag['name'])
    return tags

@my_app.route("/", methods=["GET", "POST"])
def index():
    img_data = None
    error = ""
    if request.method == "POST":
        img_url = request.form['img'] 
        try:
            tags = get_photo_tags(img_url)
            img_data = {"url": img_url, "description": tags}
        except:
            error = 'Please input a valid image URL (starting with http://).'
    
    return render_template('index.html', image=img_data, error=error)




if __name__ == '__main__':
    my_app.run(debug=True)
