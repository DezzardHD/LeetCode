use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::<i32>::with_capacity(nums.len());
        for num in nums.into_iter() {
            if (!set.insert(num)) {
                return true
            }
        }
        false
    }
}