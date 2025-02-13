impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        if (x == 0) {
            return 0;
        } else if (x == 1) {
            return 1;
        }
        
        let mut approximation: f64 = (x >> 1) as f64;
        let mut next_approximation: f64 = -1f64;
        println!("appr: {:?}", approximation);
        println!("next: {:?}", next_approximation);
        while (true) {
            next_approximation = (approximation + x as f64 / approximation) / 2f64;
            if (approximation == next_approximation) {
                break;
            }
            println!("appr: {}", approximation);
            println!("next: {}", next_approximation);
            approximation = next_approximation;
        }
        next_approximation as i32
    }
}