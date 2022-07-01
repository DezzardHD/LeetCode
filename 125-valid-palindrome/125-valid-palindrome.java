class Solution {
    public boolean isPalindrome(String s) {
        
        int a = 0;
        int tInner = s.length() - 1;
        for (int i = 0; i < s.length(); i++){
            if (Character.isLetterOrDigit(s.charAt(i))){
                for (int j = tInner; j > 0; j--){
                    if (Character.isLetterOrDigit(s.charAt(j))){
                        if (Character.toLowerCase(s.charAt(i)) == Character.toLowerCase(s.charAt(j))){
                            tInner = j - 1;
                            break;
                        }else{
                            return false;
                        } 
                    }
                    if (i>j){
                        return true;
                    }
                }
            }
        }
        return true;
    }
}