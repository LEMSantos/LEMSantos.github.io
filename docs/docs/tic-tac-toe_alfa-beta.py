from copy import deepcopy


def is_win(board, player):
    # Verificando as Linhas do Tabuleiro
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    # Verificando as Colunas do Tabuleiro
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    # Verificando as Diagonais do Tabuleiro
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    return False


def is_draw(board):
    for line in board:
        if ' ' in line:
            return False

    return True


def is_terminal(board):
    if is_win(board, CPU_PLAYER) or is_win(board, HUMAN_PLAYER) or is_draw(board):
        return True

    return False


def print_board(board):
    print('\n')

    for i, line in enumerate(board):
        print(*line, sep=' | ')

        if i != len(line) - 1:
            print('--+---+--')

    print('\n')


def candidates(board, player):
    candidate_moves = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != ' ':
                continue

            candidate = deepcopy(board)
            candidate[i][j] = player

            candidate_moves.append(candidate)

    return candidate_moves


def evaluate(board):
    if is_win(board, CPU_PLAYER):
        return 1

    if is_win(board, HUMAN_PLAYER):
        return -1

    return 0


def minimax_alpha_beta(board, alpha=float('-inf'), beta=float('+inf'), maximizing=False):
    if is_terminal(board):
        return evaluate(board)

    if maximizing:
        value = float('-inf')

        for child in candidates(board, CPU_PLAYER):
            value = max(value, minimax_alpha_beta(child, alpha, beta, False))

            if value >= beta:
                break

            alpha = max(alpha, value)
    else:
        value = float('+inf')

        for child in candidates(board, HUMAN_PLAYER):
            value = min(value, minimax_alpha_beta(child, alpha, beta, True))

            if value <= alpha:
                break

            beta = min(beta, value)

    return value


if __name__ == '__main__':
    CPU_PLAYER = 'X'
    HUMAN_PLAYER = 'O'

    human_play_first = input('Você deseja começar o jogo [s|n]: ') == 's'

    if human_play_first:
        HUMAN_PLAYER = 'X'
        CPU_PLAYER = 'O'

    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    while not is_terminal(board):
        if human_play_first:
            print_board(board)

            position = int(input('Insira a posição da jogada [1-9]: '))

            i = (position - 1) // 3
            j = (position - 1) % 3

            board[i][j] = HUMAN_PLAYER

            if is_terminal(board):
                break

        candidate_moves = candidates(board, CPU_PLAYER)
        board = max(candidate_moves, key=minimax_alpha_beta)
        human_play_first = True

    print_board(board)

    if is_win(board, HUMAN_PLAYER):
        print('Você venceu!!')
    elif is_win(board, CPU_PLAYER):
        print('Você perdeu!!')
    else:
        print('Deu Empate!!')
