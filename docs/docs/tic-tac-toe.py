from random import randint


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

        i, j = randint(0, 2), randint(0, 2)

        while board[i][j] != ' ':
            i, j = randint(0, 2), randint(0, 2)

        board[i][j] = CPU_PLAYER
        human_play_first = True

    print_board(board)

    if is_win(board, HUMAN_PLAYER):
        print('Você venceu!!')
    elif is_win(board, CPU_PLAYER):
        print('Você perdeu!!')
    else:
        print('Deu Empate!!')
