#Front end for chatbot
from flask import Flask, render_template, request
from towards_datascience import euclidean, distance
from multi import task

a = task()
Ques = a[:len(a)//2]
Ans = a[len(a)//2:]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    re = ' '.join(distance(userText))
    #fun = backend(userText)
    return re
#"<b>تھوڑا انتظار کریں۔</b>"


if __name__ == "__main__":
    app.run()
