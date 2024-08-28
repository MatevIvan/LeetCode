package LeetCode.EasyDiff;

import java.util.Arrays;

public class TwoSum {
  public static int[] twoSum(int[] nums, int target) {
    int[] solution = new int[2];
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          solution[0] = i;
          solution[1] = j;
          return solution;
        }
      }
    }
    return solution;
  }

  public static void main(String[] args) {
    int[] nums = { 3, 2, 4 };
    int[] solution = twoSum(nums, 6);
    System.out.println(Arrays.toString(solution));
  }

}
