
class Solution {
    public int romanToInt(String s) {
        ArrayList<Integer> intList = new ArrayList<Integer>();
        
        for (int i=0; i < s.length(); i++){
            intList.add(singleRomanToInt(s.charAt(i)));
        }
        int sumTmp = 0;
        for (int i = 0; i < intList.size(); i++){
            if (i != intList.size()-1){
                if (intList.get(i) >= intList.get(i+1)){
                    sumTmp += intList.get(i);
                }
                else{
                    sumTmp += intList.get(i+1)-intList.get(i);
                    i++;
                }
            } else {
                sumTmp+=intList.get(i);
            }
        }
        return sumTmp;
        }
    
    
    private int singleRomanToInt(char s){
        int n;
        switch(s){
        case 'I':n = 1;break;
        case 'V':n = 5;break;
        case 'X':n = 10;break;
        case 'L':n = 50;break;
        case 'C':n = 100;break;
        case 'D':n = 500;break;
        case 'M':n = 1000;break;
        default: n = -1;}
        
        return n;
    }
}

