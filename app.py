from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/personalities")
def personalities():
    return render_template("personalities.html")


if __name__ == "__main__":
    app.run(debug=True)
