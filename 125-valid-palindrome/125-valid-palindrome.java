class Solution {
    public boolean isPalindrome(String s) {
        
        int a = 0;
        int tInner = s.length() - 1;
        for (int i = 0; i < s.length(); i++){
            char c1 = s.charAt(i);
            if (Character.isLetterOrDigit(c1)){
                for (int j = tInner; j > 0; j--){
                    char c2 = s.charAt(j);
                    if (Character.isLetterOrDigit(c2)){
                        if (Character.toLowerCase(c1) == Character.toLowerCase(c2)){
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