from collections import defaultdict
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.cuisine_to_heap = defaultdict(list)
        self.food_to_cuisine = {}
        self.food_to_rating = defaultdict(int)
        for i in range(len(foods)):
            self.food_to_cuisine[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_to_heap[cuisines[i]], (-ratings[i], foods[i]))
            self.food_to_rating[foods[i]] = -ratings[i]
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))
        self.food_to_rating[food] = -newRating

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        smallest_lexico = None
        while len(self.cuisine_to_heap[cuisine]) > 0:
            curr = self.cuisine_to_heap[cuisine][0]
            if curr[0] != self.food_to_rating[curr[1]]:
                # delete old data
                heapq.heappop(self.cuisine_to_heap[cuisine])
                continue
            smallest_lexico = curr[1]
            break
        return smallest_lexico