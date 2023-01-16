import json
from flask import Flask

app = Flask(__name__)
with open("canditaes.json", "r", encoding="UTF-8") as file:
        datas = json.load(file)

@app.route('/')
def index():
    text = ''
    for data in datas:
        text += "Name candidates - " + data["name"] + '\n'
        text += " Position candidates - " + data["position"] + '\n'
        text += "Skills - " + data["skills"] + "\n"
    return f"<pre>{text}<pre>"

@app.route("/candidates/<name>")
def pk_candidates(name):
    for data in datas:
        if name.title().strip() in data["name"].split(" "):
            return f'<center> <img src="{data["picture"]}" width="200" height="200" alt="">\n' \
                    f'<pre> "Name candidates - " {data["name"]}\n' \
                    f'" Position candidates - "{data["position"]}\n' \
                    f'"Skills - "{data["skills"]}\n</pre>'
        elif name.title().strip() == data["name"]:
            return f'<center> <img src="{data["picture"]}" width="200" height="200" alt="">\n' \
                    f'<pre> "Name candidates - " {data["name"]}\n' \
                    f'" Position candidates - "{data["position"]}\n' \
                    f'"Skills - "{data["skills"]}\n</pre>'
    return "this candidates not found"
app.run()


