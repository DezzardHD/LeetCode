class Solution {
    public int climbStairs(int n) {
        double a = 1;
        double b = 1;
            while(n > 1){
                double tmp = a;
                a += b;
                b = tmp;
                n--;
            }
        return (int) a;
    }
}