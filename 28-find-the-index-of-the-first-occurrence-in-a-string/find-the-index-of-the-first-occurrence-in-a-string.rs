impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        for (i, c) in haystack.chars().enumerate() {
            if (i+needle.len() > haystack.len()) {break;}
            if (&haystack[i..i+needle.len()].as_bytes() == &needle.as_bytes()) {
                return i as i32;
            }
        }
        -1
    }
}