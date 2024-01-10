N = int(input())
def safe(board, row, column, n):
    for i in range(row):
        if board[i][column] == 1:
            return False
        if column - (row - i) >= 0 and board[i][column - (row - i)] == 1:
            return False
        if column + (row - i) < n and board[i][column + (row - i)] == 1:
            return False
    return True

board = [[0 for _ in range(N)] for _ in range(N)]

def generate_permutations(n, board, row):
    if row >=n:
        return 1
    count = 0   
    for i in range(n):
        if safe(board,row,i,n):
            board[row][i] = 1
            count += generate_permutations(n, board, row+1)    
            board[row][i] = 0
    return count
                                   
print(generate_permutations(N, board, 0))

