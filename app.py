''' This module is the main flask app,
     routes are defined here.'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    '''
    Returns the rendered Jinja index template on the root route.
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
