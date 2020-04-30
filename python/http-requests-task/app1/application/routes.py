# import render_template function from the flask module
from flask import render_template

# import the app object from the ./application/__init__.py
from application import app

# import APIs requests
import requests

# define routes for / & /home, this function will be called when these are accessed
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/get/animal', methods=['GET','POST'])
def animal():
    animal = requests.get('http://app2:5001/animal/name')
    noise = responses.post('http://app2:5001/animal/noise', data=animal.text)
    return Response('animals.html', title='Animals', animal=animal.text, noise=noise.text)
