impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min: i32 = prices[0];
        let mut profit: i32 = 0;
        for price in prices.into_iter() {
            if min > price {
                min = price;
            }
            if profit < price - min {
                profit = price - min;
            }
        }
        profit
    }
}