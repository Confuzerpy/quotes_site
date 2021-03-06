from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from charts import *
from datetime import datetime
import subprocess

current_datetime = datetime.now()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


"""Класс для создания бд"""


class Coin(db.Model):
    __tablename__ = 'coins'
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(100))
    name = db.Column(db.String(100))
    price_history = db.Column(db.String(10000))
    market_cap_history = db.Column(db.String(10000))
    price = db.Column(db.String(100))
    market_cap = db.Column(db.String(100))
    volume_24h = db.Column(db.String(100))
    delta_24h = db.Column(db.String(100))
    db.session.flush()
    db.session.commit()
    db.create_all()

    def __repr__(self):
        return 'Coin %r' % self.id


"""Запрещаем браузеру кэшировать"""


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


"""Главная страница"""


@app.route('/')
@app.route('/<int:page>/')
def index(page=1):
    print(1)
    search = request.args.get('search')
    # если пользователь ввёл запрос в поиск
    if search:
        if not search.isupper():
            search = search.title()
        coin = Coin.query.filter_by(name=search).first_or_404()
        price = coin.price_history
        # если минута == 0, то вызываем скрипт create_db для парсинга
        if current_datetime.minute == 0:
            subprocess.call(['python3', 'create_db.py'])
        chart_7_days(price)
        return render_template('currencies.html', coin=coin)

    page = request.args.get('page')
    # если пользователь перешёл на другую страницу
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    main = db.session.query(Coin)
    pages = main.paginate(page=page, per_page=100)
    # если минута == 0, вызываем парсер и рисуем графики
    if str(current_datetime.minute) == '00':
        subprocess.call(['python3', 'create_db.py'])
        if str(pages.items[::-1][0]) == 'Coin 100':
            count = 0
            for col in pages.items:
                count += 1
                name = col.name
                coin = Coin.query.filter_by(name=name).first()
                price = coin.price_history
                chart_7_days(price, count)

        elif str(pages.items[::-1][0]) == 'Coin 200':
            count = 100
            for col in pages.items:
                count += 1
                name = col.name
                coin = Coin.query.filter_by(name=name).first()
                price = coin.price_history
                chart_7_days(price, count)

        elif str(pages.items[::-1][0]) == 'Coin 300':
            count = 200
            for col in pages.items:
                count += 1
                name = col.name
                coin = Coin.query.filter_by(name=name).first()
                price = coin.price_history
                chart_7_days(price, count)

    return render_template('index.html', pages=pages)


"""Страница каждой монеты"""


@app.route('/currencies/<string:name>/')
def currencies(name):
    coin = Coin.query.filter_by(name=name).first_or_404()
    price = coin.price_history
    if str(current_datetime.minute) == '00':
        subprocess.call(['python3', 'create_db.py'])
    chart_7_days(price)
    return render_template('currencies.html', coin=coin)


@app.route('/about/')
def about():
    return render_template('about.html')
