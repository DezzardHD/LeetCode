impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let mut values = vec![0;26];
        for c in s1.chars().into_iter() {
            values[c as usize - 'a' as usize] += 1;
        }
        let mut left = 0;
        let mut i = 0;
        while i < s2.len() {
            values[s2.as_bytes()[i] as usize - 'a' as usize] -= 1;
            if values[s2.as_bytes()[i] as usize - 'a' as usize] >= 0 {
                if s1.len() - 1 == i - left {
                    return true;
                }
            } else {
                while values[s2.as_bytes()[i] as usize - 'a' as usize] < 0 {
                    values[s2.as_bytes()[left] as usize - 'a' as usize] += 1;
                    left += 1;
                }
            }
            i += 1;
        }
        return false
    }
}