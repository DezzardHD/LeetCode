impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        println!("{:?}", haystack.chars());
        for (i, c) in haystack.chars().enumerate() {
            if (i+needle.len() > haystack.len()) {break;}
            println!("{}",i);println!("{}",c);
            println!("{}",haystack);
            if (&haystack[i..i+needle.len()].as_bytes() == &needle.as_bytes()) {
                println!("test");
                return i as i32;
            }
        }
        -1
    }
}