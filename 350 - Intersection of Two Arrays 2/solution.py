from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)

        final = []

        for key, value in nums1_dict.items():
            if key in nums2_dict:
                if nums1_dict[key] > nums2_dict[key]:
                    final.extend([key] * nums2_dict[key])
                else:
                    final.extend([key] * nums1_dict[key])

        return final