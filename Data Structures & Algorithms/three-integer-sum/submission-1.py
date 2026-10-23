class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n) : 

            l = i+1 
            r = n - 1 
            if i > 0 and nums[i] == nums[i - 1]:
             continue
            while l<r  : 
                sum = nums[l] + nums[r] 
                if sum == -nums[i]:
                    res.append([nums[i],nums[l],nums[r]])
                    r = r-1 
                    l = l+1
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1  
                else:
                    if sum > -nums[i]: 
                        r = r-1 
                    else:
                        l = l+1

        return res

                    
                    

        