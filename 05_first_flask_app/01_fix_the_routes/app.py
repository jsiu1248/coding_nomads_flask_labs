from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    page = "Welcome to Emily's Dog Costumes!"
    return page


@app.route('/services')
def services():
    page = "I offer custom made costumes for your precious canine companion, "\
        "and a free in-home consultation, to get the measurements."
    return page

@app.route('/costumes/<costume>')
def costumes(costume):
    page = f"Check out this {costume} costume!"
    return page

if __name__ =='main':
    app.run(host="localhost", port=8000, debug=True)
