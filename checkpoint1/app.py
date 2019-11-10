from flask import Flask, render_template, request
# https://docs.clarifai.com/api-guide/train#train
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key=key)
