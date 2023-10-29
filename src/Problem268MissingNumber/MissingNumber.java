package Problem268MissingNumber;

public class MissingNumber {
    public static int missingNumber(int[] nums) {
        // xor the set of index + {n} with num in nums
        // yang sama will be 0, left with the beda one
        int result = nums.length; // u put n first so u only need to iterate over 0...n-1 in nums
        for (int i = 0; i < nums.length; i++) {
            result = result ^ i ^ nums[i];
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(missingNumber(new int[] {3,0,1}));
        System.out.println(missingNumber(new int[] {0,1}));
        System.out.println(missingNumber(new int[] {9,6,4,2,3,5,7,0,1}));
    }
}
