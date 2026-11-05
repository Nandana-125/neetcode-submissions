class Solution:
    def findMin(self, nums: List[int]) -> int:

        small = nums[0] # assume first number is the smallest 
        start = 0 
        end = len(nums) - 1 

        while start <= end : 
            mid = (start+end)//2 
            value = nums[mid]
            if small <= value : 
                # first till mid is sorted and small is the smallest value there 
                start = mid + 1 
            else : 
                small = value 
                end = mid -1 
            
        
        return small 

        