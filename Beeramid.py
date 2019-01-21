def beeramid(bonus, price):
    numberOfBeers = int(bonus/price)
    if numberOfBeers <= 0:
        return 0
    if numberOfBeers == 1:
        return 1
    for i in range(numberOfBeers+1):
        numberOfBeers -= i**2
        if numberOfBeers < 0:
            return i-1
