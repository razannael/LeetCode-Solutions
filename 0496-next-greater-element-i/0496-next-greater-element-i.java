class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        if (nums2.length == 0 || nums1.length == 0) return new int[0];
        Map<Integer, Integer> nextGr = new HashMap<>();
        Stack<Integer> stackNum = new Stack<>();
        
        // Initialize the map with the last element
        nextGr.put(nums2[nums2.length-1], -1);
        stackNum.push(nums2[nums2.length-1]);
        
        // Iterate over nums2 in reverse
        for(int i = nums2.length - 2 ; i >= 0 ; i--){
            while(!stackNum.isEmpty() && nums2[i] >= stackNum.peek()){
                stackNum.pop();
            }
            nextGr.put(nums2[i], stackNum.isEmpty() ? -1 : stackNum.peek());
            stackNum.push(nums2[i]);
        }
        
        // Fill the result for nums1 based on the map
        for(int i = 0; i < nums1.length ; i++){
            nums1[i] = nextGr.get(nums1[i]);
        }
        return nums1;
    }
}
