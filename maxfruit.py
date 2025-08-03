from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        right = 0
        n = len(fruits)
        sum = 0
        ans = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return (
                    min(
                        abs(startPos - fruits[right][0]),
                        abs(startPos - fruits[left][0]),
                    )
                    + fruits[right][0]
                    - fruits[left][0]
                )

        # each time fix the right boundary of the window
        while right < n:
            sum += fruits[right][1]
            # move left boundary
            while left <= right and step(left, right) > k:
                sum -= fruits[left][1]
                left += 1

            ans = max(ans, sum)
            right += 1

        return ans



if __name__ == "__main__":
    solution = Solution()
    fruits = [[0,10],[1,10],[2,82],[3,65],[4,29],[5,81],[6,81],[7,80],[9,50],[11,52],[13,75],[14,64],[15,40],[16,51],[17,94],[18,84],[19,5],[20,59],[21,80],[22,100],[23,29],[24,21],[25,62],[26,99],[27,73],[28,9],[29,57],[30,58],[31,59],[32,19],[33,2],[34,94],[35,69],[36,59],[37,82],[38,51],[39,86],[40,6],[42,86],[43,10],[44,12],[45,84],[46,55],[47,42],[48,11],[49,76],[51,40],[52,61],[53,60],[54,27],[56,61],[57,45],[58,20],[59,21],[60,87],[61,4],[62,1],[63,95],[64,26],[65,77],[66,50],[67,83],[68,72],[69,87],[70,28],[71,93],[72,64],[73,42],[74,26],[75,6],[76,69],[77,51],[78,29],[79,80],[80,55],[81,15],[82,50],[83,68],[84,48],[85,13],[86,4],[87,63],[88,99],[89,42],[90,18],[91,67],[92,15],[93,32],[94,37],[95,4],[96,77],[97,74],[98,41],[99,16]]
    startPos = 89
    k = 0
    result = solution.maxTotalFruits(fruits, startPos, k)
    print(f"The maximum total fruits collected is: {result}")
