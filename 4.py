import sys

def won(board):
    for row in board:
        if all(row):
            return True
    for j in range(5):
        column_full = True
        for i in range(5):
            column_full = column_full and board[i][j]
        if column_full:
            return True
    return False

def print_boards(boards):
    for b in boards:
        for row in b:
            for m in row:
                print(m, end=' ')
            print()
        print()

ns = map(int, input().split(','))
lines = list(filter(bool, map(str.strip, sys.stdin.readlines())))
boards = []
for i in range(0, len(lines) - 1, 5):
    boards += [
        [[int(x) for x in row.split()]
        for row in lines[i:i + 5]]
    ]

has_won = [False for _ in boards]
marked_boards = [[[False for _ in row] for row in board] for board in boards]
for n in ns:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, m in enumerate(row):
                if n == m:
                    marked_boards[i][j][k] = True
        if won(marked_boards[i]):
            has_won[i] = True
            if all(has_won):
                print_boards(boards)
                print_boards(marked_boards)
                print(i, n)
                total = 0
                for j, row in enumerate(board):
                    for k, m in enumerate(row):
                        if not marked_boards[i][j][k]:
                            total += m
                print(n * total)
                exit()

