class Solution {
    public int hammingDistance(int x, int y) {
        return (int) Integer.toBinaryString(x ^ y).chars().filter(c -> c == '1').count();
    }
}