class Solution {
    public boolean isAnagram(String s, String t) {
     
     if(s.length() != t.length())
     {
        return false; 
     }

     int [] count1 = new int [26]; 
     int [] count2 = new int [26]; 
     String scount , tcount;

     
     for(int i = 0 ; i < s.length(); i++)
     {
        int pos = s.charAt(i) - 'a';
        count1[pos]++; 

     }
     
     scount = Arrays.toString(count1); 
     
     for(int i = 0 ; i < t.length(); i++)
     {
        int pos = t.charAt(i) - 'a';
        count2[pos]++; 
     }
    tcount = Arrays.toString(count2); 

    if(scount.equals(tcount))
    {
        return true; 
    }

    else 

    return false; 
     

     


        

    }
}
