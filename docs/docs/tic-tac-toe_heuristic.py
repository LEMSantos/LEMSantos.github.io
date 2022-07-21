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


def evaluate_heuristic_sequence(sequence):
    number_of_blank = sequence.count(' ')
    has_two_simbols = (CPU_PLAYER in sequence and HUMAN_PLAYER in sequence)

    if number_of_blank == 3 or has_two_simbols:
        return 0

    if number_of_blank == 2:
        return 1 if CPU_PLAYER in sequence else -1

    return 10 if CPU_PLAYER in sequence else -10


def heuristic(board):
    if is_win(board, CPU_PLAYER):
        return float('+inf')

    if is_win(board, HUMAN_PLAYER):
        return float('-inf')

    score = 0

    # Avaliando as linhas do tabuleiro
    for line in board:
        score += evaluate_heuristic_sequence(line)

    # Avaliando as colunas do tabuleiro
    for j in range(len(board)):
        column = [board[i][j] for i in range(len(board))]
        score += evaluate_heuristic_sequence(column)

    # Avaliando as diagonais do tabuleiro
    main_diag = [board[i][i] for i in range(len(board))]
    secondary_diag = [board[i][j] for i, j in zip(range(3), range(2, -1, -1))]

    score += evaluate_heuristic_sequence(main_diag)
    score += evaluate_heuristic_sequence(secondary_diag)

    return score


def minimax_heuristic(board, depth=2, alpha=float('-inf'), beta=float('+inf'), maximizing=False):
    if depth==0 or is_terminal(board):
        return heuristic(board)

    if maximizing:
        value = float('-inf')

        for child in candidates(board, CPU_PLAYER):
            value = max(value, minimax_heuristic(child, depth - 1, alpha, beta, False))

            if value >= beta:
                break

            alpha = max(alpha, value)
    else:
        value = float('+inf')

        for child in candidates(board, HUMAN_PLAYER):
            value = min(value, minimax_heuristic(child, depth - 1, alpha, beta, True))

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
        board = max(candidate_moves, key=minimax_heuristic)
        human_play_first = True

    print_board(board)

    if is_win(board, HUMAN_PLAYER):
        print('Você venceu!!')
    elif is_win(board, CPU_PLAYER):
        print('Você perdeu!!')
    else:
        print('Deu Empate!!')
