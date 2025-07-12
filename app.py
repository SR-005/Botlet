from flask import Flask,request,render_template,jsonify
from dotenv import load_dotenv

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():

    #userinput=userinput.lower()
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)