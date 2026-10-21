class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map <String, List<String>> map = new HashMap<>(); 
        
         

        for(int i = 0 ; i < strs.length; i++ )
        {int count [] = new int [26]; 
            for(Char c : strs[i])
            {
                int pos = c - 'a'; 
                count[pos] ++ ; 
            }
          counts = Arrays.toString(count); 
          if(!map.containsKey(counts))
          {
            map.put(counts,new ArrayList<>()); 
          }
          map.get(counts).add(strs[i]); 
        }
    }
}
