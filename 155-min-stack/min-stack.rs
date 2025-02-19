struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        return MinStack {
            stack: Vec::new(),
            min_stack: Vec::new()
        }
    }
    
    fn push(&mut self, val: i32) {
        if self.stack.len() == 0 {
            self.min_stack.push(val);
        } else {
            if *self.min_stack.last().unwrap() > val {
                self.min_stack.push(val);
            } else {
                self.min_stack.push(*self.min_stack.last().unwrap());
            }
        }
        self.stack.push(val);
    }
    
    fn pop(&mut self) {
        self.min_stack.pop();
        self.stack.pop();
    }
    
    fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }
    
    fn get_min(&self) -> i32 {
        *self.min_stack.last().unwrap()
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */