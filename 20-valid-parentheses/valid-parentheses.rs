impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();

        for c in s.chars() {
            println!("{:?}", c);
            if c == '(' || c == '{' || c == '[' {
                stack.push(c);
            } else {
                if let Some(k) = stack.pop() {
                    if c == ')' {
                        if k != '(' {
                            return false
                        }
                    }
                    if c == '}' {
                        if k != '{' {
                            return false
                        }
                    }
                    if c == ']' {
                        if k != '[' {
                            return false
                        }
                    }
                } else {
                    return false
                }
            }
        }
        if stack.len() != 0 {
            return false
        }
        true
    }
}