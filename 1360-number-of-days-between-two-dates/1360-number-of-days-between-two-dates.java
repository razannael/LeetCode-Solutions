class Solution {
    public int daysBetweenDates(String date1, String date2) {
        return Math.abs(totalDays(date1) - totalDays(date2));
    }
        public static int totalDays(String date) {
        int year = Integer.parseInt(date.substring(0, 4));
        int month = Integer.parseInt(date.substring(5, 7));
        int days = Integer.parseInt(date.substring(8, 10));
        int[] months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        for (int i = 0; i < month - 1; i++) days += months[i];
        days += (year - 1) * 365;
        days += (year - 1) / 4;
        if (year % 4 == 0 && month > 2 && year != 2100) days++;
        return days;
    }
}