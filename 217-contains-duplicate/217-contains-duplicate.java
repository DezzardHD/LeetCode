class Solution {
    public boolean containsDuplicate(int[] nums) {
        if (nums.length == 1) return false;
        Set<Integer> hs = new HashSet();
        for (int num : nums){
            if (!hs.add(num)) return true;
        }
        return false;
    }
}