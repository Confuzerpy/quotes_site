from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Coins, Base
from parser import coinlib_pars


engine = create_engine('sqlite:///coins.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession
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
        create = Coins(symbol=symbol, name=name, price=price,
                       market_cap=market_cap, volume_24h=volume_24h,
                       delta_24h=delta_24h)
        with session() as sesi:
            sesi.add(create)
            sesi.commit()
