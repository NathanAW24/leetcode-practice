package Problem338CountingBits;

public class CountingBits {
    public static int countBitsOnInt(int n) {
        int value;
        if (n == 0) {
            value = 0;
        } else if (n == 1) {
            value = 1;
        } else {
            value = countBitsOnInt((int) ((n - 1) / 2)) + 1;
        }
        System.out.println(String.format("...countBitsOnInt num is %d, int is %d", n, value));
        return value;
    }

    public static int numberOfBits(int number) {
        if (number == 0) return 1; // Special case as log(0) is undefined
        return (int) (Math.log(number) / Math.log(2)) + 1;
    }

    public static int[] countBits(int n) {
        int[] ans = new int[n + 1];
        ans[0] = 0;
        ans[1] = 1;

        if (n == 0) {
            return new int[]{0};
        } else if (n == 1) {
            return new int[]{0, 1};
        } else { // n == 2 or more
            for (int i = 2; i <= n; i++) {
                ans[i] = ans[(int) (n - Math.pow(numberOfBits(n) - 1, 2))] + 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int n = 5;
        int[] ones = countBits(n);
        for (int i = 0; i <= n; i++) {
            System.out.println(String.format("The number is %d, bits: %d", i, ones[i]));
        }

    }
}
