import matplotlib.pyplot as plt


def chart_7_days(price, count=0):
    price = eval(price)
    len_price = len(price)
    if len_price == 7:
        last_price = float(price[6])
        pen_price = float(price[5])

        if last_price > pen_price or last_price == pen_price:
            plt.plot((1, 2, 3, 4, 5, 6, 7),
                     (float(price[0]), float(price[1]), float(price[2]),
                      float(price[3]), float(price[4]), float(price[5]),
                      float(price[6])), linewidth=3, color='limegreen')
        else:
            plt.plot((1, 2, 3, 4, 5, 6, 7),
                     (float(price[0]), float(price[1]), float(price[2]),
                      float(price[3]), float(price[4]), float(price[5]),
                      float(price[6])), linewidth=3, color='red')

    elif len_price > 7:
        price.reverse()
        price = price[:7]
        price.reverse()
        last_price = float(price[6])
        pen_price = float(price[5])
        if last_price > pen_price or last_price == pen_price:
            plt.plot((1, 2, 3, 4, 5, 6, 7),
                     (float(price[0]), float(price[1]), float(price[2]),
                      float(price[3]), float(price[4]), float(price[5]),
                      float(price[6])), linewidth=3, color='limegreen')
        else:
            plt.plot((1, 2, 3, 4, 5, 6, 7),
                     (float(price[0]), float(price[1]), float(price[2]),
                      float(price[3]), float(price[4]), float(price[5]),
                      float(price[6])), linewidth=3, color='red')

    elif len_price < 7:

        if len_price == 6:
            last_price = float(price[5])
            pen_price = float(price[4])

            if last_price > pen_price or last_price == pen_price:
                plt.plot((1, 2, 3, 4, 5, 6),
                         (float(price[0]), float(price[1]), float(price[2]),
                          float(price[3]), float(price[4]), float(price[5])),
                         linewidth=3, color='limegreen')
            else:
                plt.plot((1, 2, 3, 4, 5, 6),
                         (float(price[0]), float(price[1]), float(price[2]),
                          float(price[3]), float(price[4]), float(price[5])),
                         linewidth=3, color='red')

        elif len_price == 5:
            last_price = float(price[4])
            pen_price = float(price[3])

            if last_price > pen_price or last_price == pen_price:
                plt.plot((1, 2, 3, 4, 5),
                         (float(price[0]), float(price[1]), float(price[2]),
                          float(price[3]), float(price[4])),
                         linewidth=3, color='limegreen')
            else:
                plt.plot((1, 2, 3, 4, 5),
                         (float(price[0]), float(price[1]), float(price[2]),
                          float(price[3]), float(price[4])),
                         linewidth=3, color='red')

        elif len_price == 4:
            last_price = float(price[3])
            pen_price = float(price[2])

            if last_price > pen_price or last_price == pen_price:
                plt.plot((1, 2, 3, 4),
                         (float(price[0]), float(price[1]),
                          float(price[2]), float(price[3])),
                         linewidth=3, color='limegreen')
            else:
                plt.plot((1, 2, 3, 4),
                         (float(price[0]), float(price[1]),
                          float(price[2]), float(price[3])),
                         linewidth=3, color='red')

        elif len_price == 3:
            last_price = float(price[2])
            pen_price = float(price[1])

            if last_price > pen_price or last_price == pen_price:
                plt.plot((1, 2, 3), (float(price[0]), float(price[1]),
                                     float(price[2])),
                         linewidth=3, color='limegreen')
            else:
                plt.plot((1, 2, 3), (float(price[0]), float(price[1]),
                                     float(price[2])),
                         linewidth=3, color='red')

        elif len_price == 2:
            last_price = float(price[1])
            pen_price = float(price[0])

            if last_price > pen_price or last_price == pen_price:
                plt.plot((1, 2), (float(price[0]), float(price[1])),
                         linewidth=3, color='limegreen')
            else:
                plt.plot((1, 2), (float(price[0]), float(price[1])),
                         linewidth=3, color='red')

    if count == 0:
        plt.savefig('static/images/chart_7_d.png')
        plt.close()
    else:
        plt.xticks([])
        plt.yticks([])
        plt.savefig(f'static/images/chart_{str(count)}.png', dpi=20)
        plt.close()
