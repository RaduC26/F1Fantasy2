class TeamExport:
    def __init__(self, names, prices, total_price, total_score):
        self.__names = names
        self.__prices = prices
        self.__total_price = total_price
        self.__total_score = total_score

    def getNames(self):
        return self.__names

    def getPrices(self):
        return self.__prices

    def getTotalPrice(self):
        return self.__total_price

    def getTotalScore(self):
        return self.__total_score
