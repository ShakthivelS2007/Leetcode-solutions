from collections import Counter

class Solution:
    def minCost(self, basket1, basket2):
        cnt = Counter(basket1)
        cnt.subtract(Counter(basket2))

        swapped = []
        for num, freq in cnt.items():
            if freq % 2 != 0:
                return -1  # impossible to balance
            swapped += [num] * (abs(freq) // 2)

        if not swapped:
            return 0  # already equal

        swapped.sort()
        minNum = min(basket1 + basket2)
        half = len(swapped) // 2

        return sum(min(swapped[i], 2 * minNum) for i in range(half))


        
        
