import json
from app import app
from  flask import render_template




@app.route("/")
def home():
    with open("text.json","r")as skra4:
        data4 =json.load(skra4)
        title4 = data4["texts"]["text"]["title4"]
        text4 = data4["texts"]["text"]["About-vebside"]
    return render_template("index.html",title4 = title4,text4 = text4)

@app.route("/about")
def about():
    with open("text.json", "r") as skra:
        data = json.load(skra)
        title = data["texts"]["text"]["title"]
        text = data["texts"]["text"]["About"]
        title6 = data["texts"]["text"]["title6"]
        text6 = data["texts"]["text"]["Megaevolution"]
    return render_template("about.html",title =title,text = text, title6 = title6,text6 = text6)

@app.route("/game")
def games():
    with open("text.json", "r") as skra1:
        data1 = json.load(skra1)
        title1 = data1["texts"]["text"]["title3"]
        text1 = data1["texts"]["text"]["Video-games"]
        title5 = data1["texts"]["text"]["title5"]
        text5 = data1["texts"]["text"]["ThirdGen"]
        title7 = data1["texts"]["text"]["title7"]
        text7 = data1["texts"]["text"]["SixthGen"]
    return render_template("game.html",title1 = title1, text1 = text1,title5 = title5,text5 = text5, title7 = title7,text7 = text7)

@app.route("/series")
def series():
    with open("text.json","r") as skra2:
        data2 = json.load(skra2)
        title2 = data2["texts"]["text"]["title2"]
        text2 = data2["texts"]["text"]["Anime-series"]
    return render_template("series.html",title2 = title2, text2 = text2)


