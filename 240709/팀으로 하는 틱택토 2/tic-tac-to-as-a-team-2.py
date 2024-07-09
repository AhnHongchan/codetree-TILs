def count_team_wins(board):
    # 모든 가능한 줄을 저장
    lines = [
        # 가로줄
        board[0],
        board[1],
        board[2],
        # 세로줄
        board[0][0] + board[1][0] + board[2][0],
        board[0][1] + board[1][1] + board[2][1],
        board[0][2] + board[1][2] + board[2][2],
        # 대각선
        board[0][0] + board[1][1] + board[2][2],
        board[0][2] + board[1][1] + board[2][0]
    ]

    team_win_count = 0

    # 모든 줄을 확인하여 팀 승리 가능한 줄의 수를 계산
    for line in lines:
        unique_numbers = set(line)
        if len(unique_numbers) == 2:
            team_win_count += 1

    return team_win_count

# 입력 받기
board = [input().strip() for _ in range(3)]

# 결과 출력
print(count_team_wins(board))