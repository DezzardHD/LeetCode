use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut row: HashSet<(char, i32)> = HashSet::new();
        let mut col: HashSet<(char, i32)> = HashSet::new();
        let mut square: HashSet<(char, i32)> = HashSet::new();
        
        for ri in 0..9 {
            for ci in 0..9 {
                let boxi: i32 = (ri / 3) + (ci / 3) * 3;
                let d = board[ri as usize][ci as usize];
                if d == '.' {
                    continue;
                }
                if row.contains(&(d, ri)) || col.contains(&(d, ci)) || square.contains(&(d, boxi)) {
                    return false
                }
                row.insert((d, ri));
                col.insert((d, ci));
                square.insert((d, boxi));
            }
        }
        true
    }
}