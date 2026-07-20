class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for i , n in enumerate(nums):
            Diff = target - n
            if Diff in prevmap: 
                return [prevmap[Diff], i]
            prevmap[n] = i