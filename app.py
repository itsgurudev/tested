from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloWorld():
    ok= "fuck you!"
    return render_template("index.html", OK=ok)