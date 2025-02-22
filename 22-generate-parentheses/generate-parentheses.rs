impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut stack: Vec<String> = Vec::with_capacity((2*n) as usize);
        let mut result: Vec<String> = Vec::new();
        Solution::next(n, &mut stack, &mut result, 0, 0);
        result
    }

    fn next(n: i32, s: &mut Vec<String>, r: &mut Vec<String>, open: i32, close: i32) {
         if close > open || open > n || close > n {
            // invalid
            return
        }
        if s.len() as i32 == 2*n {
            r.push(s.join(""));
            return
        }
       

        s.push(String::from("("));
        Solution::next(n, s, r, open + 1, close);
        s.pop();
        
        
        s.push(String::from(")"));
        Solution::next(n, s, r, open, close + 1);
        s.pop();
    }
}