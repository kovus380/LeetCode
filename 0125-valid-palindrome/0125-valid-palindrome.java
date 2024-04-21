class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        StringBuffer str = new StringBuffer(s);
        return s.equals(str.reverse().toString());
    }
}