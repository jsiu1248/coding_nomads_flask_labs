from flask import Flask, render_template
from flask_bootstrap import Bootstrap


#app is an instance of a Flask object
# generally the __name__ passed as argument is correct
app=Flask(__name__)

#it is initalized by passing in the flask_bootstrap instance
#so here app is passed into the constructor
bootstrap=Bootstrap(app)

# decorator
# whenever someone visits root url then call index()

@app.route('/')

#handler
def index():
    # return "Hello World.. Is this actually working?"
    return render_template('index.html')


@app.route('/about')
def about():
    page='I hope to make either another golf related app or I wish to make the app that I have done cooler.'
    return page

#testing html for words
@app.route('/songs')
def songs():
    page='<li> Memories</li> <strong> Another</strong>'
    return page

@app.route('/song')
def song():
    song=['Memories','Chicken Fried', 'Another']
    return render_template('song.html', favorite_songs=song)


# figured out how to make a link and reroute it
@app.route('/link_page')
def link_page():
    page='<a href="/about">Link to songs</a> <a href="/songs">Link to about</a>'
    return page

# trying to run the app with
# run "export FLASK_APP=app.py" in the terminal
# "flask run" will run it.
# Go to "localhost:5000" and you will see the result

# You can turn on the debugger and it can be reloader - which reloads as you go or debugger -
# export FLASK_DEBUG=1
#testing if pushing to github

#export FLASK_ENV=development

#two dynamic arguments in a view function name and age
@app.route('/user/<name>/<age>')
def user(name, age):
    return f"Hello, {name} are you {age} years old?!"
# make another funciton that takes numeric dymnaic and return the square
@app.route('/number/<num>')
def number(num):
    return f"{int(num)**2}"
# dynamic argument with spaces

#when creating the templates folder. Make sure it is named templates and not template

@app.route('/users/<username>')
def users(username):
    return render_template('user_test.html', username1=username)

@app.route('/derived')
def derived():
    return render_template('derived.html')

@app.errorhandler(404)
def page_not_found(e):
    error_title = "Not Found"
    error_msg= "That page doesn't exist."
    return render_template('error.html', error_title=error_title, error_msg=error_msg),404 # why is there just a number here


@app.errorhandler(403)
def forbidden(e):
    error_title = "Forbidden"
    error_msg = "You shouldn't be here!"
    return render_template('error.html',
                           error_title=error_title,
                           error_msg=error_msg), 403

@app.errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template('error.html',
                           error_title=error_title,
                           error_msg=error_msg), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
