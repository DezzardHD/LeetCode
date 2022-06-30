class Solution {
    public boolean isPalindrome(int x) {
        if (x<0) return false;
        int n = x;
        int rn = 0;
        while (n>0){
            rn = rn * 10 + n % 10;
            n = n / 10;
        }
        System.out.println(rn);
        System.out.println(n);
        return rn == x;    
    }
}