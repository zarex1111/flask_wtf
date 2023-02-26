from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<string:prof>')
def courses(prof):
    return render_template('courses.html', prof=prof, title="Подготовительные пунткты")


@app.route('/list_prof/<string:list_type>')
def duties(list_type):
    with open("static/json/duties.json", encoding="utf-8") as file:
        p = json.load(file)
    return render_template("professions_list.html", list_type=list_type, duties=p, title="Список профессий")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')