class Solution {
    public String longestCommonPrefix(String[] strs) {
        String ref = strs[0];
        for (String str : strs){
            ref = compareTwoStrings(ref, str);
            if ("" == ref.replaceAll("\\s+","")){
                return "";
            }
        }
        return ref.replaceAll("\\s+","");
        
    }
    
    private String compareTwoStrings(String ref, String sample){
        int maxLength = ref.length() > sample.length() ? ref.length() : sample.length();
        String spaces = "";
        
        for (int i = 0; i < maxLength; i++){
            spaces += " ";
        }
        
        if (ref.length() != maxLength){
            ref += spaces;
        } else if (sample.length() != maxLength){
            sample += spaces;
        }
        int idx = maxLength;
        for (int i = 0; i < maxLength; i++){
            if (ref.charAt(i) != sample.charAt(i)){
                idx = i;
                break;
            }   
        }
        
        spaces = "";
        for (int i = 0; i < maxLength-idx; i++){
            spaces += " ";
        }
        return ref.substring(0,idx) + spaces;
    }
}