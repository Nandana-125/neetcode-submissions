class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map< Integer, Integer> map = new HashMap <>(); 
        int[] sol  = new int[k]; 
        int j = 0 ; 
        for (int i = 0; i <nums.length; i ++)
        {
            map.put(nums[i], map.getOrDefault(nums[i],0)+1);  
        }
 
        for(Map.Entry<Integer, Integer> entry : map.entrySet())
        { 
            if(entry.getValue()>=k)
            {
               sol[j] = entry.getKey(); 
               j++; 
            }

        }

        return sol; 
    }
}
