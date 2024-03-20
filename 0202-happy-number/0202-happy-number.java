class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while(n != 1 &&  !seen.contains(n)){
            seen.add(n);
            n = next(n);
        }
        return n == 1;
    }
    private int next (int n){
        int sum = 0;
        int d ;
        while(n > 0){
            d = n % 10;
            n = n / 10;
            sum += d*d;
        }
        return sum;
    }
}