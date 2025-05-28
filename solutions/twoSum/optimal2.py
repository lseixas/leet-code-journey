from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for index, number in enumerate(nums):

            if hashMap.get(number, None):
                return [hashMap[number], index]

            hashMap[number-target] = index

        return []