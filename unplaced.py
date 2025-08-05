from typing import List

class Solution(object):
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced

if __name__ == "__main__":
    solution = Solution()
    fruits = [4,2,5]
    baskets = [3,5,4]
    result = solution.numOfUnplacedFruits(fruits, baskets)

    print(f"The number of unplaced fruits are {result}")
