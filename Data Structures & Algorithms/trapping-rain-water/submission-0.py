class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        m_l = 0 
        max_left = [0] * n 
        # max left 
        for i in range (n) :
            max_left[i] = m_l 
            m_l = max(m_l, height[i]) 

         
        # max right 
        m_r = 0 
        max_right = [0] * n 

        for i in range (n-1 , -1 , -1 ):
            max_right[i] = m_r
            m_r = max(m_r, height[i])
        
        
        # calculating water blocks  formula is min(l and r) - height of the index 
        sum = 0
        mi = [0] * n
        for i in range(n):
          mi[i] = min(max_left[i],max_right[i]) - height[i]

        for i in range (n):
          if mi[i]<=0:
            continue
          sum = sum + mi[i] 
        
        return sum


