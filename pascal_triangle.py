
from typing import List


def generate(numRows: int) -> List[List[int]]:
    
    if numRows <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(numRows)]

    for i in range(2, numRows):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle

result=generate(5)  # Example usage
print(result)  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]