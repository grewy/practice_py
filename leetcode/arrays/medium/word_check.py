
def word_check(board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

def dfs(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j >= len(board[0]) or j < 0 or board[i][j] != word[0]:
        return False
    tmp = board[i][j]
    #mark visited
    board[i][j] = '#'
    #check all possible direction for dfs to check for next letter of word
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1,j, word[1:]) or dfs(board, i,j+1, word[1:]) or dfs(board,i,j-1,word[1:])
    board[i][j] = tmp
    return res



board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]

word = 'ABCCED'
print word_check(board, word)
print word_check(board, 'SEE')
print word_check(board, 'ABCB')

