from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route("/name")
def name():
    return "Hello, my name is Flask!"
@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

app.run(debug=True)