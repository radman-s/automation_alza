import math

def count_dph(val):
    coeff = 21 / 100
    dph = float(val) * coeff
    all = float(dph) + float(val)
    return float(all)

cn = count_dph(25619)
print(math.floor(cn))

