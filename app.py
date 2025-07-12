from flask import Flask,request,render_template,jsonify

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    botreply=""
    if request.method == "POST":
        userinput=request.form.get("userinput")
        userinput=userinput.lower()
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)