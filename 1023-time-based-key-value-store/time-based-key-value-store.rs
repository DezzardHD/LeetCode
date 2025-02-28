use std::collections::HashMap;

struct TimeMap {
    pub map: HashMap<String, Vec<(i32, String)>>
}


/**ap<Str 
 * Some(value) => v =  `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {

    fn new() -> Self {
        return TimeMap {
            map: HashMap::new(),
        }
    }
    
    fn set(&mut self, key: String, value: String, timestamp: i32) {
        if let Some(v) = self.map.get_mut(&key) {
            v.push((timestamp, value));
        } else {
            self.map.insert(key, vec![(timestamp, value)]); 
        }
        // println!("{:?}", self.map);
    }
    
    fn get(&self, key: String, timestamp: i32) -> String {
        let v: &Vec<(i32, String)>;
        match self.map.get(&key) {
            Some(value) => v = value,
            None => return "".to_string()
        }
        
        let mut l: i32 = 0;
        let mut r: i32 = v.len() as i32 - 1;
        
        let mut res: String = "".to_string();
        while l <= r {
            let m: i32 = (r - l) / 2 + l;
            if v[m as usize].0 <= timestamp {
                res = v[m as usize].1.clone();
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        res
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */