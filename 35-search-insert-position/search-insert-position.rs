impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut low: usize = 0;
        let mut high: usize = nums.len() - 1;
        
        while (low != high) {
            let mut k: usize = low + (high - low + 1) / 2;
            if (nums[k] <= target) {
                low = k;
            } else {
                high = k - 1;
            }
        }
        if (nums[high] != target) {
            if (nums[0] > target) {
                high = 0;
            } else {
                high += 1;
            }
        }
        high as i32
    }
}