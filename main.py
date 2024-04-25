import json
from flask import Flask, render_template

app = Flask('213.87.139.94')

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)


@app.route("/list_prof/<sp>")
def list_prof(sp):
    file = open("conf.txt", encoding="utf-8")
    data = file.readlines()
    file.close()
    return render_template("list_prof.html", sp=sp, data=data)


@app.route("/distribution")
def dis():
    sp = ["Ридли Скотт",
          "Энди Уир",
          "Марк Уотни",
          "Венката Капур",
          "Тедди Сандерс",
          "Шон Бин "]
    return render_template("distribution.html", sp=sp)


@app.route("/table/<sex>/<age>")
def table(sex, age):
    return render_template("table.html", sex=sex, age=int(age))


@app.route("/member")
def member():
    file = open("list_of_astr.json", encoding="utf-8")
    data = file.read()
    data = json.loads(data)
    file.close()
    return render_template("card.html", data=data)


def main():
    app.run()


if __name__ == '__main__':
    main()
