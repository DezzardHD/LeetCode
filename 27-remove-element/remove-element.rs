impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut counter = 0;
        let len = nums.len();
        for i in 0..len {
            if nums[i] != val {
                nums[counter] = nums[i];
                counter += 1;
            }
        }
        counter as i32
    }
}