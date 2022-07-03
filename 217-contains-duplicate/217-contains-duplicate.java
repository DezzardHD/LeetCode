class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> hs = new HashSet<Integer>();
        for (int num : nums){
            if (!hs.add(num)) return true;
        }
        return false;
    }
}