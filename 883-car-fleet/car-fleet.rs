use std::iter::zip;

impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut cars = Vec::from_iter(position.into_iter().zip(speed));
        cars.sort();
        let mut count = 0;
        let mut time = 0f64;
        for car in cars.iter().rev() {
            let mut curr_time: f64 = (target - car.0) as f64 / car.1 as f64;
            if time < curr_time{
                count = count + 1;            
                time = curr_time;
            }
        }
        count
    }
}