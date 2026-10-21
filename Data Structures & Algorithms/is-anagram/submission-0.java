class Solution {
    public boolean isAnagram(String s, String t) {
        
        int [] count1 = new int[26];
        int [] count2 = new int [26];

        for(int i = 0 ; i< s.length();i++)
        {
            count1[s.charAt(i) -'a']++;
        }
        for(int i = 0 ; i< t.length();i++)
        {
            count2[t.charAt(i)-'a']++;
        }

       return Arrays.equals(count1, count2);
    }
}
