use std::collections::HashMap;
use std::cmp::max;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut map: HashMap<char, i32> = HashMap::new();
        let mut start: i32 = 0;
        let mut maximum: i32 = 0;
        for (i, c) in s.chars().into_iter().enumerate() {
            if let Some(v) = map.get(&c) {
                start = max(start, map.get(&c).unwrap() + 1);
            }
            map.insert(c, i as i32);
            maximum = max(i as i32 + 1 - start, maximum);
        }
        return maximum
    }
}