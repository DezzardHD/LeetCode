impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        s.trim_end().split(' ').next_back().map_or(0, |word| word.len() as i32)
    }
}