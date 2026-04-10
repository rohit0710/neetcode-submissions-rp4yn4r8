/**
 * Definition of Interval:
 * class Interval(var start: Int, var end: Int) {}
 */

class Solution {
    fun canAttendMeetings(oldIntervals: List<Interval>): Boolean {
        val intervals = oldIntervals.sortedBy { it.start }
        for (i in 1 until intervals.size) {
            println(intervals[i].start)
            if (intervals[i].start < intervals[i-1].end)
                return false
        }
        return true


    }
}
