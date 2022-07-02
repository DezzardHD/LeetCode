class Solution {
    public int climbStairs(int n) {
        double result = 0;
        for (int i = 0; i <= n / 2; i++){
            result += factorial(n - i) / factorial(n - 2 * i) / factorial(i);
        }
        return (int) result;
    }
    
    private double factorial(int n){
        double result = 1; 
        for (int i = n; i > 0; i--){
            result *= i;
        }
        return result;
    }
}