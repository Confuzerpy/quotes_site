import matplotlib.pyplot as plt
# from app import *


def chart_7_days(price, count=0):
    price = eval(price)
    len_price = len(price)
    if len_price == 7:
        plt.plot((1, 2, 3, 4, 5, 6, 7),
                 (float(price[0]), float(price[1]), float(price[2]),
                  float(price[3]), float(price[4]), float(price[5]),
                  float(price[6])))

    elif len_price > 7:
        price = price.reverse()
        price = price[:7]
        plt.plot((1, 2, 3, 4, 5, 6, 7),
                 (float(price[0]), float(price[1]), float(price[2]),
                  float(price[3]), float(price[4]), float(price[5]),
                  float(price[6])))

    elif len_price < 7:
        if len_price == 6:
            plt.plot((1, 2, 3, 4, 5, 6),
                     (float(price[0]), float(price[1]), float(price[2]),
                      float(price[3]), float(price[4]), float(price[5])))

        elif len_price == 5:
            plt.plot((1, 2, 3, 4, 5),
                     (float(price[0]), float(price[1]), float(price[2]),
                      float(price[3]), float(price[4])))

        elif len_price == 4:
            plt.plot((1, 2, 3, 4),
                     (float(price[0]), float(price[1]),
                      float(price[2]), float(price[3])))

        elif len_price == 3:
            plt.plot((1, 2, 3), (float(price[0]), float(price[1]),
                                 float(price[2])))

        elif len_price == 2:
            plt.plot((1, 2, 3), (float(price[0]), float(price[1])))

    # plt.show()
    if count == 0:
        plt.savefig('static/images/chart_7_d.png')
    else:
        plt.xticks([])
        plt.yticks([])
        plt.savefig(f'static/images/chart_{str(count)}.png')
