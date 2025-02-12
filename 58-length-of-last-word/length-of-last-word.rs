impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        if let Some(word) = s.trim_end().split(' ').next_back() {
            return word.len() as i32
        }
        0
    }
}