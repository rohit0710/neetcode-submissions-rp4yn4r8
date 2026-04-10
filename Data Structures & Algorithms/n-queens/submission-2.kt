class Solution {
    fun solveNQueens(n: Int): List<List<String>> {
        var board = MutableList(n) { MutableList(n) {"."} }
        fun isSafe(r: Int, c: Int): Boolean
        {
            for(i in 0 until c)
                if(board[r][i] == "Q")
                    return false

            for ((i,j) in (r downTo 0).zip(c downTo 0))
                if(board[i][j] == "Q")
                    return false

            for ((i,j) in (r until n).zip(c downTo 0))
                if(board[i][j] == "Q")
                    return false

            return true
        }
        var res : MutableList<List<String>> = mutableListOf()
        fun backTrack(col: Int){
            if (col >= n)
            {
                res.add(board.map {it.joinToString("")})
            }
            for (row in 0 until n)
                if (isSafe(row, col)) {
                    board[row][col] = "Q"
                    backTrack(col + 1)
                    board[row][col] = "."
                }
        }

        backTrack(0)
        return res

    }
}
