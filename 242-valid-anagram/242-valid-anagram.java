class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        HashMap<Character, Integer> hm = new HashMap();
        for (int i = 0; i < s.length(); i++){
            if (hm.containsKey(s.charAt(i))){
                hm.replace(s.charAt(i), hm.get(s.charAt(i)) + 1);
            } else {
                hm.put(s.charAt(i), 1);
            }
        }
        for (int i = 0; i < s.length(); i++){
            if (hm.containsKey(t.charAt(i))){
                hm.replace(t.charAt(i), hm.get(t.charAt(i)) - 1);
            } else {
                return false;
            }
        }
        Iterator iter = hm.values().iterator();
        while (iter.hasNext()){
            if (!iter.next().equals(0)) return false;
        }
        return true;
    }
}