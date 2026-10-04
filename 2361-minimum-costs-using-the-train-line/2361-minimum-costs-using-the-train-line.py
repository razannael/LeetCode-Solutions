class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        @cache
        def dp(stopType: str, stopNumber: int) -> int:
            if stopNumber == 0:
                # In case we want to arrive at station 1 using express route, we need to pay the cost of switching immediately
                return expressCost if stopType == 'E' else 0
            
            if stopType == 'R':
                # Come from previous regular station using regular route
                option_1 = regular[stopNumber - 1] + dp('R', stopNumber - 1)
                # Come from previous express station and switch to regular route
                option_2 = regular[stopNumber - 1] + dp('E', stopNumber - 1)
                return min(option_1, option_2)
            else:
                # Come from previous express station using express route
                option_1 = express[stopNumber - 1] + dp('E', stopNumber - 1)
                # Come from previous regular station by switching to express route
                option_2 = express[stopNumber - 1] + expressCost + dp('R', stopNumber - 1)
                return min(option_1, option_2)

        return [min(dp('R', stopNumber), dp('E', stopNumber)) for stopNumber in range(1, len(regular) + 1)]

    