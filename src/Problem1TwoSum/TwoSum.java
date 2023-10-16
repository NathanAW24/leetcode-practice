package Problem1TwoSum;

import java.util.HashMap;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (hm.containsKey(target - nums[i])) {
                int[] ans = {i, hm.get(target - nums[i])};
                return ans;
            } else {
                hm.put(nums[i], i);
            }
        }
        return new int[2];
    }
    public static void main(String[] args) {
        int[] result = twoSum(new int[]{2,7,11,15}, 9);
        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }

}
