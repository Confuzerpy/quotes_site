# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from flask_sqlalchemy import SQLAlchemy
from app import *
from parser import coinlib_pars


# engine = create_engine('sqlite:///coins.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coins.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# db = app.db
lst_coins = coinlib_pars()


for coins in lst_coins:
    coins_dct = coins['coins']
    for coin in coins_dct:
        symbol = coin['symbol']
        name = coin['name']
        price = coin['price']
        market_cap = coin['market_cap']
        volume_24h = coin['volume_24h']
        delta_24h = coin['delta_24h']
        create = Coin(symbol=symbol, name=name, price=price,
                      market_cap=market_cap, volume_24h=volume_24h,
                      delta_24h=delta_24h)
        db.session.add(create)
        db.session.flush()
        db.session.commit()
        # with session() as sesi:
        #     sesi.add(create)
        #     sesi.commit()
