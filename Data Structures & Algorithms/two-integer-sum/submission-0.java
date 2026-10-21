class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map <Integer, Integer> map = new HashMap <>(); 
        int [] result = new int [2];
        int diff; 
        for(int i = 0 ; i< nums.length; i++){

            diff = target - nums[i]; 

            if(map.containsKey(diff))
            {
                result[0] = i ; 
                result[1] = map.get(diff);
                break ; 
            }

            else
            map.put(diff, i);
        }

        return result; 
    }
}
