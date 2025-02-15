use std::collections::HashMap;
use std::vec::Vec;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<Vec<i32>, Vec<String>> = HashMap::new();

        for s in strs.into_iter() {
            let mut v: Vec<i32> = vec![0; 26];
            for c in s.chars() {
                v[(u32::from(c) - u32::from('a')) as usize] += 1;
            }
            if let Some(list) = map.get_mut(&v) {
                list.push(s);
            } else {
                map.insert(v, vec![s]);
            }
            

        }
        map.into_values().collect()
    }
}