class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        di = {}
        res = []
        diff = 0 
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in di :
                res.append(di.get(diff))
                res.append(i)
            di[nums[i]] = i 

        return res 

