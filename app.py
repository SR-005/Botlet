from flask import Flask,request,render_template,jsonify
from chatbot import main as botautomation

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    botreply=None
    userinput=None
    if request.method == "POST":
        pass
        #getting message from the user
        userinput=request.form.get("userinput")
        #userinput="tell me a joke"
        print(userinput)
        botreply=botautomation(userinput)
        print(botreply)
    return render_template("index.html")
    
if __name__=="__main__":
    app.run(debug=True)