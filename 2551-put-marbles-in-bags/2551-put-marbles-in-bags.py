class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        Find the difference between maximum and minimum scores when distributing marbles into k bags.
        
        Args:
            weights: A list of integers representing weights of marbles
            k: The number of bags to distribute marbles into
            
        Returns:
            The difference between maximum and minimum scores
            """

        # Edge case: if k=1 or k=len(weights), there's only one way to distribute
        if k == 1 or  k == len(weights):
            return 0

        # For each potential cut between positions i and i+1, calculate the cost
        # This cost equals weights[i] + weights[i+1]
        pair_sums = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i+1])

        #Sort the pair nums
        pair_sums.sort()

        # We need to make k-1 cuts
        # For minimum score: use the k-1 smallest pair sums as cut points
        # For maximum score: use the k-1 largest pair sums as cut points
        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])

        # Note: The first and last elements of weights always contribute to the total cost
        # regardless of how we split (they're always endpoints of bags)
        # So they don't affect the difference between max and min scores
        
        
        return max_score - min_score
