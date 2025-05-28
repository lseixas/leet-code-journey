from typing import List


class Solution:

    #would work if sorted was allowed and the answer indexes could be changed
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        head = len(nums) - 1
        tail = 0

        nums.sort()
        
        while True:

            if nums[tail] + nums[head] == target:
                return [tail, head]
            if nums[tail] + nums[head] > target:
                head-=1
            if nums[tail] + nums[head] < target:
                tail+=1

            if tail == head:
                return []