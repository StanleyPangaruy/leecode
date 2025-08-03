from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged = []

        merged.extend(nums1)
        merged.extend(nums2)
        merged.sort()

        # n = len(nums1)
        # m = len(nums2)

        mergelen = len(merged)
        oddeven = mergelen % 2


        if oddeven == 1:
            center = mergelen//2
            median = merged[center]
            return median
        else:
            center1 = mergelen//2
            center2 = mergelen//2 - 1
            median = (merged[center1] + merged[center2]) / 2
            return median

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"The median of the two sorted arrays {nums1} and {nums2} is: {result}")