impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        nums.dedup();
        println!("{:?}", nums);
        nums.len() as i32
    }
}