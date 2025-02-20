impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut ops: Vec<i32> = Vec::new();
        let mut nums: Vec<i32> = Vec::new();
        let mut left: i32;
        let mut right: i32;
        
        for t in tokens.iter() {
            if "*/+-".contains(t) {
                let right = nums.pop().unwrap();
                let left = nums.pop().unwrap();
                let res = match t.as_str() {
                    "*" => left * right,
                    "/" => left / right,
                    "+" => left + right,
                    "-" => left - right,
                    _ => panic!("Invalid operator"),
                    };
                nums.push(res);
            } else {
                let num: i32 = t.parse().unwrap();
                nums.push(num);
            }
        }
        return nums[0]
    }
}