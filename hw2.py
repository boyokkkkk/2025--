def last_remaining_inference(board):
    res=[[[0]*9 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for num in range(1,10):
                    if if_unique_valid(board,i,j,num)==True:
                        res[i][j][num-1]=1
    return res

def if_unique_valid(board,i,j,num):
    # 判断行内其余格可不可以填
    for col in range(9):
        if col!=j and board[i][col]==num:
            return False
    # 判断列
    for row in range(9):
        if row!=i and board[row][j]==num:
            return False
    # 判断宫
    box_r=(i//3)*3
    box_c=(j//3)*3
    for u in range(box_r,box_r+3):
        for v in range(box_c,box_c+3):
            if (u!=i or v!=j) and board[u][v]==num:
                return False

    return True

def possible_number_inference(board):
    res=[[[1]*9 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j]!=0:
                for num in range(9):
                    res[i][j][num]=0
                res[i][j][board[i][j]-1]=1

    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                # 遍历未填单元格所在列（根据确定值排除）
                for col in range(9):
                    if board[i][col]!=0:
                        res[i][j][board[i][col]-1]=0
                # 遍历所在行
                for row in range(9):
                    if board[row][j]!=0:
                        res[i][j][board[row][j]-1]=0
                # 遍历宫格
                box_r=(i//3)*3
                box_c=(j//3)*3
                for u in range(box_r,box_r+3):
                    for v in range(box_c,box_c+3):
                        if board[u][v]!=0:
                            res[i][j][board[u][v]-1]=0

    return res

test_board = [
    [0, 7, 0, 4, 0, 8, 0, 2, 9],
    [0, 0, 2, 0, 0, 0, 0, 0, 4],
    [8, 5, 4, 0, 2, 0, 0, 0, 7],
    [0, 0, 8, 3, 7, 4, 2, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 2, 6, 1, 7, 0, 0],
    [0, 0, 0, 0, 9, 3, 6, 1, 2],
    [2, 0, 0, 0, 0, 0, 4, 0, 3],
    [1, 3, 0, 6, 4, 2, 0, 7, 0]
]


last_res=last_remaining_inference(test_board)
possible_res=possible_number_inference(test_board)

print('Last Remaining Cell Result:\n')
for i in range(9):
    for j in range(9):
        print(f'Cell ({i},{j}):{[k+1 for k,v in enumerate(last_res[i][j]) if v==1]}')

print('---------------------------------------')

print("Possible Number Inference Result:\n")
for i in range(9):
    for j in range(9):
        print(f'Cell ({i},{j}):{[k+1 for k,v in enumerate(possible_res[i][j]) if v==1]}')


