class Solution {
    public int openLock(String[] deadends, String target) {
        // Initialize sets for the beginning and end states, and the deadends
        Set<String> begin = new HashSet(), end = new HashSet(), deads = new HashSet();
        // Add all deadends to the deads set
        Collections.addAll(deads, deadends);
        // If the initial state is a deadend, return -1
        if (deads.contains("0000")) return -1;

        // Add the initial state to the begin set and the target state to the end set
        begin.add("0000");
        end.add(target);
        // Initialize a counter for the number of steps
        int count = 0;

        // While there are still states to process in both the begin and end sets
        while (!begin.isEmpty() && !end.isEmpty()) {
            // Swap the begin and end sets if the begin set is larger than the end set
            while (begin.size() > end.size()) {
                Set<String> temp = begin;
                begin = end;
                end = temp;
            }

            // Initialize a set to store the next states
            Set<String> tempSet = new HashSet();
            // For each state in the begin set
            for (String s : begin) {
                // If the end set contains the current state, return the count
                if (end.contains(s)) return count;
                // Add the current state to the deads set
                deads.add(s);
                // Add all next states of the current state to the tempSet
                tempSet.addAll(getNext(s, deads));
            }
            // Increment the count
            count += 1;
            // Update the begin set to the tempSet
            begin = tempSet;
        }
        // If no solution is found, return -1
        return -1;
    }

    private List<String> getNext(String s, Set<String> deads) {
        // Initialize a list to store the next states
        List<String> ans = new ArrayList();
        // Convert the current state to a char array
        char[] arr = s.toCharArray();

        // For each digit in the current state
        for (int i = 0; i < arr.length; i++) {
            // Store the original digit
            char temp = arr[i];

            // Increment the digit, wrapping around to 0 if it's 9
            arr[i] = arr[i] == '9' ? '0' : ++arr[i];
            // Convert the updated state to a string
            String str = new String(arr);
            // Restore the original digit
            arr[i] = temp;
            // If the updated state is not a deadend, add it to the ans list
            if (!deads.contains(str)) {
                ans.add(str);
            }

            // Decrement the digit, wrapping around to 9 if it's 0
            arr[i] = arr[i] == '0' ? '9' : --arr[i];
            // Convert the updated state to a string
            String str1 = new String(arr);
            // Restore the original digit
            arr[i] = temp;
            // If the updated state is not a deadend, add it to the ans list
            if (!deads.contains(str1)) {
                ans.add(str1);
            }
        }
        // Return the list of next states
        return ans;
    }
}