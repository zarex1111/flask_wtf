from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<string:prof>')
def courses(prof):
    return render_template('courses.html', prof=prof, title="Подготовительные пунткты")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')