from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
  return redirect(url_for('code_404'))
  #return render_template("portfolio.html")


@app.route("/not_found")
def code_404():
  return render_template("404.html"), 404