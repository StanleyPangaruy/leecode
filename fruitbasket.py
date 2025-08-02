
from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter()
        m = float("inf")
        for b1 in basket1:
            freq[b1] += 1
            m = min(m, b1)
        for b2 in basket2:
            freq[b2] -= 1
            m = min(m, b2)

        merge = []
        for k, c in freq.items():
            if c % 2 != 0:
                return -1
            merge.extend([k] * (abs(c) // 2))

        if not merge:
            return 0
        merge.sort()
        return sum(min(2 * m, x) for x in merge[: len(merge) // 2])


# Example usage:
if __name__ == "__main__":
    basket1 = [4,4,4,4,3]
    basket2 = [5,5,5,5,3]
    solution = Solution()

print(solution.minCost(basket1, basket2))