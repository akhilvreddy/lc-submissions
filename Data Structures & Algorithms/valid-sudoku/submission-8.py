class Solution:
    """
    plan:

    we need 3 different data structures to keep track of the row, the column, and the square
    the data structure should be a dict of hashsets
    row || key -> current row
    col || key -> current col
    square || key -> current square (row // 3, col // 3)

    iterate through the 2d matrix and check if element is empty. if empty, then continue

    if not empty, then check if the element is already part of that row's set or that column's set or that square's set. if yes -> instantly return Fasle
    else continue adding to dict

    finally return true
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                currVal = board[r][c]

                # check if empty element
                if (currVal == "."): 
                    continue

                # check if exists in the grid already
                if (
                    (currVal in rows[r]) or 
                    (currVal in cols[c]) or 
                    (currVal in squares[(r // 3, c // 3)]) 
                ):
                    return False

                # add to dict
                else: 
                    rows[r].add(currVal)
                    cols[c].add(currVal)
                    squares[(r //3, c // 3)].add(currVal)

        return True