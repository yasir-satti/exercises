# import request & Response function from the flask module
from flask import request, Response

# import the app object from the ./application/__init__.py
from application import app

from random import randint

# define routes for /animal/name & /animal/noise, this function will be called when these are accessed
@app.route('/animal/name', methods = ['GET'])
def animal_name():
    animals = ['cat', 'dog', 'cow']
    return Response(animals[randint(0,2)], mimetype='text/plain')

@app.route('/animal/noise', methods=['POST'])
def animal_noise():
    animal = request.data.decode("utf-8")
    if animal == "cat":
        noise = "meow"
    elif animal =="dog":
        noise = "woof"
    elif animal =="cow":
        noise = "mooo"
    else:
        noise = "Do not know this animal"
    return Response(noise, mimetype='text/plain')
