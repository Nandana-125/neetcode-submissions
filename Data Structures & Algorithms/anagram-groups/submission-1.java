class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map <String, List<String>> map = new HashMap<>(); 
        List<List<String>> list = new ArrayList<>(); 
         

        for(int i = 0 ; i < strs.length; i++ )
        {int count [] = new int [26]; 
        String counts; 
            for(int j = 0 ; j < strs[i].length(); j++)
            {  char c = strs[i].charAt(j); 
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

        for(Map.Entry <String, List<String>> entry : map.entrySet() )
        {
            list.add(entry.getValue());
        }
    return list ; 
    }
}
