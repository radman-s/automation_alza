import math

def count_dph(val):
    coeff = 21 / 100
    dph = float(val) * coeff
    all = float(dph) + float(val)
    return math.floor(float(all))





