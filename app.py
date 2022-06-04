from flask import Flask

#app is an instance of a Flask object
# generally the __name__ passed as argument is correct
app=Flask(__name__)

# decorator
# whenever someone visits root url then call index()

@app.route('/')

#handler
def index():
    return "Hello World"

