import java.util.Arrays;

class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length == 1) {
            return nums;
        }

        int mid = nums.length / 2;
        int[] left = sortArray(Arrays.copyOfRange(nums, 0, mid));
        int[] right = sortArray(Arrays.copyOfRange(nums, mid, nums.length));

        return merge(left, right);
    }

    private int[] merge(int[] left, int[] right) {
    ArrayList<Integer> result = new ArrayList<>();

    int i = 0, j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            result.add(left[i]);
            i++;
        } else {
            result.add(right[j]);
            j++;
        }
    }

    for (; i < left.length; i++) {
        result.add(left[i]);
    }
    for (; j < right.length; j++) {
        result.add(right[j]);
    }

    return result.stream().mapToInt(k -> k).toArray();
}

}