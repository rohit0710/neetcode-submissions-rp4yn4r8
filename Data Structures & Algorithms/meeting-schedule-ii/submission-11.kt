/**
 * Definition of Interval:
 * class Interval(var start: Int, var end: Int) {}
 */

class Solution {
    fun minMeetingRooms(intervals: List<Interval>): Int {
        if (intervals.isEmpty())
            return 0
        val newIntervals = intervals.sortedBy {it.start}
        val pq = PriorityQueue<Int>()
        pq.add(newIntervals[0].end)

        for (i in 1 until intervals.size)
        {
            if(newIntervals[i].start < pq.peek())
                pq.add(newIntervals[i].end)
            else
            {
                val pop = pq.poll()
                pq.add(max(pop, newIntervals[i].end))
            }
            
        }
        return pq.size
    }
}
