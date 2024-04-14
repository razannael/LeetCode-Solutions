import java.util.PriorityQueue;
import java.util.Comparator;

public class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(Comparator.comparingInt(a -> -(a[0]*a[0] + a[1]*a[1])));
        
        for (int[] point : points) {
            maxHeap.add(point);
            if (maxHeap.size() > K) {
                maxHeap.poll();
            }
        }
        
        int[][] result = new int[K][2];
        while (K > 0) {
            result[--K] = maxHeap.poll();
        }
        
        return result;
    }
}
