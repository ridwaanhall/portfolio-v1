from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
  return url_for('error')
  #return render_template("portfolio.html")


@app.route("/404qweqweqwewqeqw")
def error():
  return "404"