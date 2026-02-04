from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]

        print("Merged and sorted array:", nums1)
        
        n = len(nums1)
        if n % 2 == 1:
            median = nums1[n//2]
        else:
            median = (nums1[n//2 - 1] + nums1[n//2]) / 2
        print("Median:", median)
        return median


n, m = map(int, input("Length of n and m: ").split())

nums1 = [int(input("Enter nums1 value: ")) for _ in range(n)]
nums2 = [int(input("Enter nums2 value: ")) for _ in range(m)]

obj = Solution()
obj.findMedianSortedArrays(nums1, nums2)
