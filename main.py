from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)