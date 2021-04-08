from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""3 класса, отвечающие за создание бд. Запускаем питон,
импортируем db и вводим db.create_all()"""


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


# class Coin_now(db.Model):
#     __tablename__ = 'coins_now'
#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.String(100))
#     market_cap = db.Column(db.String(100))
#     volume_24h = db.Column(db.String(100))
#     delta_24h = db.Column(db.String(100))
#     db.session.flush()
#     db.session.commit()
#     db.create_all()

#     def __repr__(self):
#         return 'Coin_now %r' % self.id


# class Coin_history(db.Model):
#     __tablename__ = 'coins_history'
#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.String(1000))
#     market_cap = db.Column(db.String(1000))
#     db.session.flush()
#     db.session.commit()
#     db.create_all()

#     def __repr__(self):
#         return 'Coin_history %r' % self.id


"""Главная страница"""


@app.route('/')
@app.route('/<int:page>/')
def index(page=1):
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    main = db.session.query(Coin)  # .all()
    pages = main.paginate(page=page, per_page=100)

    return render_template('index.html', pages=pages)


"""Страница монет"""


@app.route('/currencies/<string:name>/')
def currencies(name):
    # curr = request.args.get('')
    print(type(name))
    coin = Coin.query.filter_by(name=name).first()
    print(coin)
    print(type(coin))
    return render_template('currencies.html', coin=coin)
