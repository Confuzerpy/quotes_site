from flask import Flask, render_template, request
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from database_setup import Coins
# from parser import coinlib_pars


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
    # print('db is create')

    # def create_db(self):
    #     lst_coins = coinlib_pars()
    #     for coins in lst_coins:
    #         coins_dct = coins['coins']
    #         for coin in coins_dct:
    #             symbol = coin['symbol']
    #             name = coin['name']
    #             price = coin['price']
    #             market_cap = coin['market_cap']
    #             volume_24h = coin['volume_24h']
    #             delta_24h = coin['delta_24h']
    #             create = Coins(symbol=symbol, name=name, price=price,
    #                            market_cap=market_cap, volume_24h=volume_24h,
    #                            delta_24h=delta_24h)
    #             db.session.add(create)
    #             db.session.flush()
    #             db.session.commit()
    #     engine = create_engine('sqlite:///coins.db')
    #     Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()

"""Главная страница"""


@app.route('/')
def index():
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    main = db.session.query(Coin)  # .all()
    pages = main.paginate(page=page, per_page=100)

    return render_template('index.html', pages=pages)
