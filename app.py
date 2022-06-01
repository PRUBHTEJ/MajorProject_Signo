from flask import Flask
from flask import render_template
from flask import request
import os

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main():
    if request.method=="GET":
        return render_template("frontend.html")
    elif request.method=="POST":
        os.system("python3 Application.py")
        return render_template("frontend.html")
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=False)
