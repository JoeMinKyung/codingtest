from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    memo = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in memo:
            return [memo[needed], i]
        memo[num] = i

#nums=[4,1,9,7,5,3,16]
nums=[4,1,9,7,8,2]
target=14

print(twoSum(nums=nums,target=target))

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         memo={}
#         for v in nums:
#             memo[v]=True
#         for v in nums:
#             needed_num=target-v
#             if needed_num in memo:
#                 return True
#         return False
        
