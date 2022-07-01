class Solution {
    public boolean isPalindrome(String s) {
        String s1 = "";
        String s2 = "";
        for (int i = 0; i < s.length(); i++){
            if (Character.isLetterOrDigit(s.charAt(i))){
                s1 += s.charAt(i);
            }
            if (Character.isLetterOrDigit(s.charAt(s.length() - 1 - i))){
                s2 += s.charAt(s.length() - 1 - i); 
            }
        }
        
        System.out.println(s1.toLowerCase());
        System.out.println(s2.toLowerCase());
        return s1.toLowerCase().equals(s2.toLowerCase());
    }
}