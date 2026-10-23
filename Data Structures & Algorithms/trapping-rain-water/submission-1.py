class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = 0 
        max_right = 0 
        l = 0 
        r = n-1
        res = [0] * n 

        for i in range(n):
            max_left = max(max_left , height [l])
            max_right = max(max_right, height[r])
            #calculating the threshold 
            if max_left <= max_right : 
                val = max_left - height[l] 
                l = l+1 
                if val <=0 :
                    res[i] = 0 
                else : 
                    res[i] = val
            else :
                  val = max_right - height[r]
                  r = r-1
                  if val <=0 :
                    res[i] = 0 
                  else : 
                    res[i] = val 
        sum = 0 
        for i in range(n):
            sum = sum+ res[i]
        return sum





            
        