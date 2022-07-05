class Solution {
    public boolean isValid(String s) {
        char c = s.charAt(0);
        Stack<Character> stk = new Stack<Character>();
        if (!(c == '(' || c == '[' || c == '{')) return false;
        for (int i = 0; i < s.length(); i++){
            c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{'){
                stk.push(c);
            } else {
                if(stk.empty()) return false;
                if (stk.peek() == '(' && c == ')') {
                    stk.pop();
                    continue;
                }
                if (stk.peek() == '[' && c == ']') {
                    stk.pop();
                    continue;
                }
                if (stk.peek() == '{' && c == '}') {
                    stk.pop();
                    continue;
                }
                return false;
            }
        }
        return stk.empty();
    }
}