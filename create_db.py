from app import *
from parser import coinlib_pars


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
