import numpy as np


def calc_next(l):
    ll = len(l)
    input_data = []
    output_data = []
    n = ll // 2
    for i in range(n, ll):
        input_data.append(l[i - n: i])
        output_data.append([l[i]])
    inp = input
    x = input_data
    x = np.linalg.inv(x)
    y = output_data
    res = np.matmul(x, y)
    return np.matmul([l[-n:]], res)


def get_price_perc():
    l = []
    f = open('data.txt', 'r')
    data = f.readline().strip()
    while data:
        x = list(map(int, data.split()))
        l.append((x[0] - x[1]) / x[1] * 100)
        data = f.readline().strip()
    return l


l = get_price_perc()
print(l)
print(calc_next(l))