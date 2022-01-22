from flask import Flask, render_template
app = Flask(__name__)
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

@app.route("/")
def home():
    return render_template('index.html',params=params)

@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/project")
def contact():
    return render_template('project.html', params=params)


app.run(debug=True)

