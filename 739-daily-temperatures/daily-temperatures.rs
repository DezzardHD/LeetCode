impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![0; temperatures.len()];
        let mut stack: Vec<(i32, i32)> = Vec::new();

        for (i, temp) in temperatures.iter().enumerate() {
            while !stack.is_empty() && *temp > (*stack.last().unwrap()).0 {
                let (temp2, index) = stack.pop().unwrap();
                res[index as usize] = (i as i32) - (index as i32);
            }
            stack.push((*temp, i as i32));
        }
        res
    }
}