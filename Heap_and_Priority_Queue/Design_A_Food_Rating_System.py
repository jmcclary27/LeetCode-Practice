class FoodRatings:
    import heapq

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisinesDict = {}
        self.currentRating = {}
        self.match = {}
        for i in range(len(foods)):
            if cuisines[i] not in self.cuisinesDict:
                self.cuisinesDict[cuisines[i]] = []
            heapq.heappush(self.cuisinesDict[cuisines[i]], (-1 * ratings[i], foods[i]))
            self.currentRating[foods[i]] = ratings[i]
            self.match[foods[i]] = cuisines[i]

    def changeRating(self, food: str, newRating: int) -> None:
        self.currentRating[food] = newRating
        heapq.heappush(self.cuisinesDict[self.match[food]], (-1 * newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisinesDict[cuisine]:
            rate, item = self.cuisinesDict[cuisine][0]
            if rate * -1 == self.currentRating[item]:
                return item
            self.cuisinesDict[cuisine].pop()
        return "None"