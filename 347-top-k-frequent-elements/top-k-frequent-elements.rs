use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut count  = HashMap::new();
        let mut freq: Vec<Vec<i32>> = vec![vec![]; nums.len()];

        for num in nums.iter() {
            count.entry(num).and_modify(|c| {*c += 1}).or_insert(1);
        }

        for (num, count) in count.into_iter() {
            freq[count as usize - 1usize].push(*num);
        }

        let mut res: Vec<i32> = Vec::with_capacity(k as usize);
        for i in (0..(freq.len())).rev() {
            for num in &freq[i] {
                res.push(*num);
            }
            if res.len() as i32 == k {
                return res
            }
        }
        
        vec![1]
    }
}