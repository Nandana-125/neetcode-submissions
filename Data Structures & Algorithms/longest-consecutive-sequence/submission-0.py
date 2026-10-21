class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for n in num_set:
            count = 0
            if n - 1 not in num_set:
               temp = n
            else:
               continue

            while temp in num_set:
                count = count + 1 
                temp =  temp+1

            res = max(res, count)


        return res  