def find_min_board_size(N, W, H) -> int: 
    # N - cards count, W - width, H - height
    board = [[1]]
    counter = 0
    i = 1
    while i < N:
        counter += 1
        if len(board[0]) * W < len(board) * H:
            for j in range(len(board)):
                board[j].append(1)
                counter += 1

                i += 1
                if i >= N:
                    break
        
        else:
            board.append([])
            for j in range(len(board[0])):
                board[-1].append(1)
                counter += 1

                i += 1
                if i >= N:
                    break

    print(counter)

    return max(len(board[0]) * W, len(board) * H)