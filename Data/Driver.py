class Member:
    def __init__(self, name, current_price, season_score, price_history, points_history, is_constructor):
        self.name = name
        self.current_price = current_price
        self.season_score = season_score
        self.price_history = price_history
        self.points_history = points_history
        self.is_constructor = is_constructor

    def getRacePrice(self, race_no):
        return self.price_history[race_no]

    def getName(self):
        return self.name

    def getCurrentPrice(self):
        return self.current_price

    def getSeasonScore(self):
        return self.season_score

    def isConstructor(self):
        return self.is_constructor
