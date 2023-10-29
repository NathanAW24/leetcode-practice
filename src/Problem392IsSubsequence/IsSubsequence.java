package Problem392IsSubsequence;

public class IsSubsequence {
    public static boolean isSubsequence(String s, String t) {
        // edge case where s lebih gede dari t
        if (s.length() > t.length()) {
            return false;
        }

        // in this case s pasti lebih keci atau sama panjang
        // i is s_pointer, j is t_pointer
        int i = 0, j = 0;
        while (j < t.length() && i < s.length()) {
            if (s.charAt(i) == t.charAt(j)) { // idx out of range here
                i++; // i ++ only when there is match
            }
            j++; // j ++ whenever match or not
        }

        // if s "abc" is substring of "abcd" for example,
        // the i pointer will jump three times, ending at index after c (at s.length())
        return i == s.length();
    }

    public static void main(String[] args) {
        System.out.println(isSubsequence("abc", "ahbgcd"));
        System.out.println(isSubsequence("axc","ahbgcd"));
    }

}
