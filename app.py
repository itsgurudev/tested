from flask import Flask, render_template, request#, session
#from flask_session import Session

app = Flask(__name__)

#app.config["SESSION_PERMANENT"]=False
#app.config["SESSION_TYPE"]="filesystem"
#Session(app)

notelist=[]


@app.route('/')
def index():
    names=notelist
    return render_template("index.html", names=names)

@app.route('/bye')
def bye():
    names=["don't", "do", "this", "to", "me", "fuck", "this", "shit", 56]
    return render_template("index.html", names=names)


@app.route('/calc')
def calc():
    return render_template("calc.html")

@app.route('/result', methods=["GET", "POST"])
def result():
    result=0
    num=0
    if request.method == "POST":
        num=request.form.get("num")
        if num=="":
            num=0
        num=float(num)
        result= num*num
        
    return render_template("result.html",num=num, result=result)
   
@app.route('/notes', methods=["GET", "POST"])
def notes():   
    if request.method == "POST":
        note=request.form.get("note")
        notelist.append(note)  
    return render_template("notes.html",notelist=notelist)


