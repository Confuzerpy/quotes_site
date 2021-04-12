from app import *
from list_test import *
from parser import coinlib_pars
from datetime import datetime

lst_coins = coinlib_pars()
# lst_coins = lst
current_datetime = datetime.now()

count = 0
for coins in lst_coins:
    count += 1
    print(count)
    coins_dct = coins['coins']

    for cur_coin in coins_dct:
        symbol = cur_coin['symbol']
        name = cur_coin['name']

        if current_datetime.hour == 23:
            coin = Coin.query.filter_by(name=name).first()

            coin.symbol = symbol
            coin.name = name
            # coin_id = coin.id
            """всё, что закоментированно - юзать только при первом запуске,
            если бд пустая"""
            # lst_price = []
            # lst_market_cap = []
            # lst_price_history = lst_price.append(cur_coin['price'])
            # lst_price_history = str(lst_price)
            # coin.price_history = lst_price
            # lst_market_cap_history = lst_market_cap.append(cur_coin['market_cap'])
            # lst_market_cap_history = str(lst_market_cap)
            # coin.market_cap_history = lst_market_cap

            lst_price_history = eval(coin.price_history)
            lst_market_cap_history = eval(coin.market_cap_history)

            price_history = cur_coin['price']

            if float(price_history) == 1000 or float(price_history) > 1000:
                price_history = price_history.split('.')[0]
            else:
                price_history = str(round(float(price_history), 2))

            market_cap_history = cur_coin['market_cap']
            market_cap_history = market_cap_history.split('.')[0]

            lst_price_history.append(price_history)
            lst_price_history = str(lst_price_history)
            coin.price_history = lst_price_history

            lst_market_cap_history.append(market_cap_history)
            lst_market_cap_history = str(lst_market_cap_history)
            coin.market_cap_history = lst_market_cap_history

            price = cur_coin['price']

            if float(price) == 1000 or float(price) > 1000:
                price = price.split('.')[0]
                coin.price = price
            else:
                price = round(float(price), 2)
                coin.price = str(price)

            market_cap = cur_coin['market_cap']
            market_cap = market_cap.split('.')[0]
            coin.market_cap = market_cap

            volume_24h = cur_coin['volume_24h']
            volume_24h = volume_24h.split('.')[0]
            coin.volume_24h = volume_24h

            delta_24h = cur_coin['delta_24h']
            coin.delta_24h = delta_24h

            # create = Coin(symbol=symbol, name=name, price=price,
            #               price_history=lst_price_history,
            #               market_cap_history=lst_market_cap_history,
            #               market_cap=market_cap, volume_24h=volume_24h,
            #               delta_24h=delta_24h)
            # db.session.add(create)
            # db.session.flush()
            db.session.commit()

        else:
            coin = Coin.query.filter_by(name=name).first()

            coin.symbol = symbol
            coin.name = name

            price = cur_coin['price']
            if float(price) == 1000 or float(price) > 1000:
                price = price.split('.')[0]
                coin.price = price
            else:
                price = round(float(price), 2)
                coin.price = str(price)

            market_cap = cur_coin['market_cap']
            market_cap = market_cap.split('.')[0]
            coin.market_cap = market_cap

            volume_24h = cur_coin['volume_24h']
            volume_24h = volume_24h.split('.')[0]
            coin.volume_24h = volume_24h

            delta_24h = cur_coin['delta_24h']
            coin.delta_24h = delta_24h

            # price = cur_coin['price']
            # market_cap = cur_coin['market_cap']
            # volume_24h = cur_coin['volume_24h']
            # delta_24h = cur_coin['delta_24h']
            # lst_price = str(lst_price)
            # lst_market_cap = str(lst_market_cap)
            # create = Coin(symbol=symbol, name=name, price=price,
            #               market_cap=market_cap, volume_24h=volume_24h,
            #               delta_24h=delta_24h)
            # db.session.add(create)
            # db.session.flush()
            db.session.commit()
