class Solution {
    public boolean isPalindrome(String s) {
        char[] chars = s.toCharArray();
        String s1 = "";
        String s2 = "";
        for (char c : chars){
            if (Character.isLetterOrDigit(c)){
                s1 += c;
                s2 = c + s2;
            }
        }
        return s1.toLowerCase().equals(s2.toLowerCase());
    }
}