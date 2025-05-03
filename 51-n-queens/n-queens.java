class Solution {
    
    private int n;
    private List<List<Integer>> tmpResult = new ArrayList();
    
    public List<List<String>> solveNQueens(int n) {
        this.n = n;
        
        explore(new ArrayList());

        List<List<String>> res = new ArrayList();
        String rowTemplate = ".".repeat(this.n);
        for (List<Integer> currentList : this.tmpResult) {
            List<String> tmpList = new ArrayList();
            for (int val : currentList) {
                StringBuilder sb = new StringBuilder(rowTemplate);
                sb.setCharAt(calculateColumn(val), 'Q');
                tmpList.add(sb.toString());
            }
            res.add(tmpList);
        }
        return res;
    }

    private void explore(List<Integer> positions) {
        if (positions.size() == this.n) {
            tmpResult.add(List.copyOf(positions));
            return;
        }
        
        for (int i = 0; i < this.n; i++) {
            int position = positions.size() * this.n + i;
            if (isValidPosition(position, positions)) {
                positions.add(position);
                explore(positions);
                positions.remove(positions.size() - 1);
            }
        }
    }

    private boolean isValidPosition(int position, List<Integer> positions) {
        return isEmptyColumn(position, positions) && areEmptyDiagonals(position, positions);
    }

    private boolean isEmptyColumn(int position, List<Integer> positions) {
        for (int val : positions) {
            if (calculateColumn(position) == calculateColumn(val)) {
                return false;
            }
        } 
        return true;
    }

    private int calculateColumn(int position) {
        return position % this.n;
    }

    private boolean areEmptyDiagonals(int position, List<Integer> positions) {
        return isEmptyDiagonal(this.n + 1, position, positions) &&
               isEmptyDiagonal(this.n - 1, position, positions);
    }

    private int calculateRow(int position) {
        return position / this.n;
    }

    private boolean isEmptyDiagonal(int decreaseBy, int pointer, List<Integer> positions) {
        for (int i = 0; i < positions.size(); i++) {
            int previousRow = calculateRow(pointer);
            pointer -= decreaseBy;
            int currentRow = calculateRow(pointer);
            if (pointer < 0 || previousRow - currentRow != 1) {
                break;
            }
            if (positions.contains(pointer)) {
                return false;
            }
        }
        return true;
    }
}
