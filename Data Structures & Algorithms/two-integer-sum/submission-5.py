class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        di = {}
        diff = 0 
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in di :
                return [di[diff], i]
            di[nums[i]] = i 

        return null

