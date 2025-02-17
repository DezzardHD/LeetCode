impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut prefix: Vec<i32> = Vec::with_capacity(nums.len());
        let mut suffix: Vec<i32> = Vec::with_capacity(nums.len());
        let mut output: Vec<i32> = Vec::with_capacity(nums.len());
        prefix.push(1);
        suffix.push(1);
        for i in 0..(nums.len() - 1usize) {
            prefix.push(nums[i] * prefix[i]);
            suffix.push(nums[nums.len() - 1usize - i] * suffix[i]);
        }
        for i in 0..(nums.len()) {
            output.push(prefix[i]*suffix[nums.len() - 1usize - i]);
        }
        output
    }
}