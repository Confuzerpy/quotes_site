from app import *
from list_test import *
from parser import coinlib_pars
from datetime import datetime

# lst_coins = coinlib_pars()
lst_coins = lst
current_datetime = datetime.now()

for coins in lst_coins:
    coins_dct = coins['coins']
    for cur_coin in coins_dct:
        symbol = cur_coin['symbol']
        name = cur_coin['name']
        # print(name)
        if current_datetime.hour == 23:
            coin = Coin.query.filter_by(name=name).first()
            coin.symbol = symbol
            coin.name = name
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

            coin_id = coin.id
            lst_price_history = eval(coin.price_history)
            lst_market_cap_history = eval(coin.market_cap_history)
            price_history = cur_coin['price']
            market_cap_history = cur_coin['market_cap']
            lst_price_history.append(price_history)
            lst_price_history = str(lst_price_history)
            coin.price_history = lst_price_history
            lst_market_cap_history.append(market_cap_history)
            lst_market_cap_history = str(lst_market_cap_history)
            coin.market_cap_history = lst_market_cap_history
            price = cur_coin['price']
            coin.price = price
            market_cap = cur_coin['market_cap']
            coin.market_cap = market_cap
            volume_24h = cur_coin['volume_24h']
            coin.volume_24h = volume_24h
            delta_24h = cur_coin['delta_24h']
            coin.delta_24h = delta_24h
            create = Coin(symbol=symbol, name=name, price=price,
                          price_history=lst_price_history,
                          market_cap_history=lst_market_cap_history,
                          market_cap=market_cap, volume_24h=volume_24h,
                          delta_24h=delta_24h)
            db.session.add(create)
            db.session.flush()
            db.session.commit()

        else:
            coin = Coin.query.filter_by(name=name).first()
            coin.symbol = symbol
            coin.name = name
            price = cur_coin['price']
            coin.price = price
            market_cap = cur_coin['market_cap']
            coin.market_cap = market_cap
            volume_24h = cur_coin['volume_24h']
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

            # print(coin.market_cap_history)

            # name_id = coin.id()

            # print('lst', lst_price_history)
            # print('type', type(lst_price_history))
            # for i in coin:
            #     print(i)
            # print('name', type(coin))
            # print(coin['name'])
            # print(name_id)
            # print('id', type(name_id))
            # нужно юзать eval(), чтобы достать список из строки






# symbol = 'test'
# name = 'tess'
# price_history = str([1,24,55,252])
# market_cap_history = 'market_cap'
# price = 'price'
# market_cap = 'market_cap'
# volume_24h = 'volume_24h'
# delta_24h = 'delta_24h'
# create = Coin(symbol=symbol, name=name, price=price,
#                       price_history=price_history,
#                       market_cap_history=market_cap_history,
#                       market_cap=market_cap, volume_24h=volume_24h,
#                       delta_24h=delta_24h)
# db.session.add(create)
# db.session.flush()
# db.session.commit()
