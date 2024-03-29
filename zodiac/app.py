from datetime import date
from wsgiref.validate import validator
from flask import Flask, render_template, abort, url_for, redirect, session, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    # the validator is needed because a string is required
    name = StringField("What is your name?", validators=[DataRequired()])
    #stores as a datetime.date
    birthday = DateField("What is your birthday?", format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField("Submit")


#app is an instance of a Flask object
# generally the __name__ passed as argument is correct
app=Flask(__name__)

# Flask object has dictionary built in for config variables
#will store this at a safer place later
app.config['SECRET_KEY'] = "keep it secret, keep it safe"

#it is initalized by passing in the flask_bootstrap instance
#so here app is passed into the constructor
bootstrap=Bootstrap(app)

# decorator
# whenever someone visits root url then call index()

# adding methods that it accepts
@app.route('/', methods=['GET','POST'] )

#handler
def index():
    # return "Hello World.. Is this actually working?"
    #shows the form
    form = NameForm()
    # name=None # we need a session variable now instead
    if form.validate_on_submit():
        session['name']= form.name.data

        # name=form.name.data # we can clear the line because it already gets cleared
        form.name.data=""
        #whenever a post function happens then you can go back to get function so it doesn't error
        flash('Please enjoy this place!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/about')
def about():
    page='I hope to make either another golf related app or I wish to make the app that I have done cooler.'
    return page

#testing html for words
@app.route('/songs')
def songs():
    page='<li> Memories</li> <strong> Another</strong>'
    return page

@app.route('/zodiac', methods=["GET", "POST"])
def zodiac():
    # creating form
    form = NameForm()
    print(f'xx {form.validate_on_submit()}')
    if form.validate_on_submit():
        # a session object is a dictionary object
        # name is a session variable and setting it equal to the form's name's data.
        session['name']= form.name.data
        # date is a session variable and setting it equal to the form's birthday data
        session['date']=form.birthday.data
        form_date=session['date']
        # new variable for storing animal name
        zodiac_animal = zodiac_year(form_date)
        flash("Your zodiac sign is "+zodiac_animal)
        return redirect(url_for('zodiac'))
    #
    return render_template('zodiac.html', form=form, name=session.get('name'),
    date_year=session.get('date_year'))

def zodiac_year(user_date):
    """Find zodiac animal based on birth year.
    The input is a datetime object and the output is a string."""

    zodiac_dict = {"Rat":1948, "Ox":1949, "Tiger":1950, "Rabbit":1951, "Dragon":1952,
    "Snake":1953, "Horse":1954, "Goat":1955, "Monkey":1956, "Rooster":1957, "Dog":1958,"Pig":1959}

    # extracting the year portion from the datetime from the user
    date_year=user_date.year
    while True:
        # if date_year in zodiac_dict then loop over the dictionary.
        if date_year in zodiac_dict.values():
            for animal, date in zodiac_dict.items():

                # if the date
                if date == date_year:
                    zodiac_animal = animal
            break
        else:
            # if the date_year isn't in zodiac year, then decrease by 12
            date_year = date_year - 12
    return zodiac_animal

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
    # this is because of a flask response object that 500 is just a parameter
    return render_template('error.html',
                           error_title=error_title,
                           error_msg=error_msg), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
