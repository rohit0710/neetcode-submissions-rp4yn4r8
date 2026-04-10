class Solution {
    fun solveNQueens(n: Int): List<List<String>> {
        val board = Array(n) { Array(n) {"."} }
        fun isSafe(row: Int, col: Int):Boolean {

            for (c in 0 .. col-1)
                if(board[row][c] == "Q")
                    return false

            for((r,c) in (row downTo 0).zip( col downTo 0))
                if(board[r][c] == "Q")
                    return false
            for((r,c) in (row .. n-1).zip( col downTo 0))
                if(board[r][c] == "Q")
                    return false
            return true
        }
        var res = mutableListOf<List<String>>()
        fun backTrack(col: Int) {
            if (col >= n)
                res.add(board.map { it.joinToString("")})

            for (row in 0 .. n-1)
                if (isSafe(row, col))
                {
                    board[row][col] = "Q"
                    backTrack(col + 1)
                    board[row][col] = "."
                }
        }
        backTrack(0)
        return res
    }
}
