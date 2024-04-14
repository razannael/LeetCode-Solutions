
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int ans[][] = new int[k][2];
        PriorityQueue<Point> pq = new PriorityQueue<>((a, b) -> {
            return ((b.a * b.a) +( b.b * b.b)) - ((a.a * a.a) + (a.b * a.b));
        });
        for (int i = 0; i < points.length; i++) {
            Point p = new Point();
            p.a = points[i][0];
            p.b = points[i][1];
            pq.add(p);
            if (pq.size() > k) {
                pq.remove();
            }
        }
        int i = 0;
        while (!pq.isEmpty()) {
            Point p = pq.poll();
            ans[i][0] = p.a;
            ans[i][1] = p.b;
            i++;
        }

        return ans;

    }

    class Point {
        int a;
        int b;
    }
}