from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Coin(db.Model):
    __tablename__ = 'coins'
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(100))
    name = db.Column(db.String(100))
    price = db.Column(db.String(100))
    market_cap = db.Column(db.String(100))
    volume_24h = db.Column(db.String(100))
    delta_24h = db.Column(db.String(100))
    # add_time = db.Column(db.DateTime(), default=datetime.utcnow)
    db.session.flush()
    db.session.commit()
    db.create_all()

    def __repr__(self):
        return 'Coin %r' % self.id


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


@app.route('/currencies/<string:name>/')
def currencies(name):
    # curr = request.args.get('')
    print(name)
    coin = Coin.query.filter_by(name=name).first()
    print(coin)
    return render_template('currencies.html', coin=coin)
