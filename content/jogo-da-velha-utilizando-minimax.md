Title: Jogo da velha com o Minimax
Date: 2022-07-17 09:03
Modified: 2022-07-17 09:03
Category: Inteligência Artificial
Tags: Minimax, Python, Busca, Inteligência Artificial
Slug: jogo-da-velha-utilizando-minimax
Authors: Lucas Eliaquim
Description: Nesse artigo vamos aprender a construir o algorítimo minimax para jogar o jogo da velha, e além disso, vamos aprender como otimizar a abordagem ingênua através da poda alfa-beta e da utilização de heurísticas.
Status: draft


![React: JavaScript library](/images/tictactoe.png)
<p style="text-align: center; margin-top: -27px"><em><a href="https://www.freepik.com/vectors/robot-chatbot" target="_blank">Robot chatbot vector created by upklyak - www.freepik.com</a></em></p>


Bom dia, Boa tarde ou Boa noite (dependendo da hora que você está lendo esse artigo),


## Vá direto ao assunto...

- [Preparando o jogo da velha](#preparando-o-jogo-da-velha)
- [O Minimax](#o-minimax)
    - [Implementando a abordagem ingênua](#implementando-a-abordagem-ingenua)
    - [Otimizando com a poda Alfa-Beta](#otimizando-com-a-poda-alfa-beta)
    - [Aprimorando ainda mais com heurísticas](#aprimorando-ainda-mais-com-heuristicas)
- [Recapitulando](#recapitulando)


<a id="preparando-o-jogo-da-velha"></a>

## Preparando o jogo da velha

O jogo da velha, cerquilha, jogo do galo ou tic-tac-toe é um jogo/passatempo muito popular (joguei muito quando era pequeno). Ele possui regras bem simples. A ideia geral é que tendo um tabuleiro 3 x 3, cada jogador escolhe um símbolo, tipicamente "X" ou "O", e cada um dele faz uma jogada por turno. O jogador que conseguir colocar 3 símbolos iguais em linha, coluna ou diagonal vence o jogo. Caso isso não seja possível e as jogadas se esgotem, o jogo acaba em empate.

Bom, para que possamos implementar o nosso algoritmo invencível no jogo da velha, precisamos primeiro ter um jogo da velha (hehehehe). Então, vamos contruir uma versão bem simples utilizando Python e deixá-lo pronto para que possamos enfrentar o computador.

Vamos precisar de algumas funções úteis:

- Função para verificar se um determinado jogador venceu
- Função para verificar se houve empate
- Função para verificar se o jogo acabou
- Por último, uma função para imprimir na tela o nosso tabuleiro

Após implementar-mos essas funções é só montar a lógica do nosso jogo.

Vamos começar com a função para determinar um vencedor:

```python
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
```

Eu sei que tem muitos IFs, mas eu tentei fazer da forma mais didática possível para facilitar o entendimento. Basicamente estamos verificando todas as linhas, colunas e diagornais, para checar se o **`player`** formou uma sequência. Em caso positivo retornamos **`True`**, e **`False`** caso contrário.

Em seguida precisamos verificar o empate:

```python
def is_draw(board):
    for line in board:
        if ' ' in line:
            return False

    return True
```

Para definir se houve empate ou não, basta ver todas as linha, se houver algum espaço em branco significa que o jogo ainda não acabou. Em seguida vamos definir uma função para verificar se o jogo foi finalizado:

```python
def is_terminal(board):
    if is_win(board, CPU_PLAYER) or is_win(board, HUMAN_PLAYER) or is_draw(board):
        return True

    return False
```

Essa função vai nos ajudar a simplificar o nosso código e também vai ser útil quando estivermos implementando o Minimax. Ainda não se preocupe com as variáveis **`CPU_PLAYER`** e **`HUMAN_PLAYER`**, elas serão definidas em outro momento, apenas pense nelas como o símbolo que identifica cada jogador, no nosso caso **`X`** e **`O`**.

Por último, mas não menos importante, precisamos da função que vai desenhar o nosso tabuleiro:

```python
def print_board(board):
    print('\n')

    for i, line in enumerate(board):
        print(*line, sep=' | ')

        if i != len(line) - 1:
            print('--+---+--')

    print('\n')
```

Com as funções necessárias já finalizadas, agora podemos montar a nossa lógica de jogo.

```python
from random import randint

# ...
# AQUI FICARIAM AS OUTRAS FUNÇÔES
# ...

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
```

Com a lógica de jogo finalizada, sinta-se a vontade para testar. Nessa parte, enquanto não temos o nosso algoritmo inteligente, fazemos o computador realizar jogadas aleatórias com o trecho:

```python
i, j = randint(0, 2), randint(0, 2)

while board[i][j] != ' ':
    i, j = randint(0, 2), randint(0, 2)

board[i][j] = CPU_PLAYER
```

Se for da sua preferência você ainda pode colocar um trecho, após a última função **`print_board`**, para entregar uma mensagem amigável ao usuário, como ilustrado abaixo.

```python
if is_win(board, HUMAN_PLAYER):
    print('Você venceu!!')
elif is_win(board, CPU_PLAYER):
    print('Você perdeu!!')
else:
    print('Deu Empate!!')
```

O código completo dessa parte do jogo da velha você pode encontrar [nesse link](/docs/tic-tac-toe.py){target="_blank"}.

Bom, código implementado e tudo funcional, ta na hora de pensar em deixar o nosso computador um pouco mais inteligênte.


<a id="o-minimax"></a>

## O Minimax

O Minimax é um algoritmo baseado em árvore que trabalha de forma recursiva e é utilizado em teoria da decisão e teoria dos jogos. Ele fornece um movimento ótimo para o jogador, considerando que o oponente também joga de forma ótima. Ele geralmente é utilizado para implementar IA em jogos, como Xadrez, Jogo da Velha, e vários outros jogos de dois jogadores.

O Minimax intuitivamente constrói uma árvore para a tomada de decisão levando em consideração todas as jogadas possíveis. Essa árvore muitas vezes é difícil de ser percebida, dado que ela é feita através de recursividade, onde muita abstração é necessária.

Todos os nossos exemplos de utilização do Minimax vão levar em consideração o jogo da velha.

Imagine a seguinte situação, o seu nome é **MAX** e o seu oponente se chama **MIN**. Você está em um jogo bem complicado e é a sua vez. Uma forma comum de pensar seria: Se eu, MAX jogar na posição x, o MIN pode jogar em y ou z, e dai então eu...

Esse tipo de pensamento pode ser modelado como uma árvore de decisão como visto abaixo.

![Árvore gerada pelo Minimax](/images/minimax-tree.png){width=75%}

Olhando dessa forma, podemos escolher uma jogada e saber exatamente quais as consequências dessa escolha.

Agora precisamos de alguma forma identificar onde o jogo termina e atribuir uma pontuação adequada. No nosso caso vamos colocar **`+1`** sempre que o **`MAX`** vencer, **`-1`** para o caso de vitória do **`MIN`** e **`0`** no empate. Essas pontuações podem ser alteradas, mas é importante de alguma forma fazer com que a vitória seja mais vantajosa que a derrota. Assim, para representar essa importância colocamos números positivos, negativos e neutros, introduzindo então, uma lógica matemática.

![Árvore gerada pelo Minimax com pontuação nas folhas](/images/minimax-tree-punctuation.png){width=75%}

No caso do nosso exemplo não tivemos situações de empate, mas é importante sempre lembrar de colocar todas as pontuações corretas.

Agora vamos propagar a nossa pontuação para os estados superiores para saber qual é a melhor jogada para escolher. Pense agora que sempre que o **`MAX`** vai fazer a jogada ele quer maximizar as suas chances e por isso sempre escolhemos a maior pontuação para ser propagada. Já no caso da jogada do **`MIN`**, ele quer minimizar as chances do **`MAX`** e assim sempre escolhe a menor pontuação a ser propagada.

![Árvore gerada pelo Minimax com propagação da pontuação](/images/minimax-tree-propagation.png){width=75%}

Agora o **`MAX`** tem 3 possibilidades de escolha, uma com pontuação **`+1`** e duas com **`-1`**. Como o **`MAX`** é esperto e quer sempre escolher a melhor jogada possível, a jogada escolhida será a demonstrada abaixo. Assim, como consequência dessa escolha, o **`MAX`** vence o jogo.

![Jogada vencedora escolhida](/images/win-strategy.png){width=25%}

Seguindo esse exemplo nós acabamos de definir o comportamento esperado do Minimax.

Sendo uma pessoa esperta, imagino que você deve ter notado que se em algum estado a pontuação estiver negativa, significa que em algum momento na subárvore existe pelo menos uma possibilidade de derrota. Deve ter percebido também que só é interessante seguir esse caminho quando não temos nenhuma opção melhor como uma vitória ou um empate. De forma análoga, se existe um ramo com pontuação positiva, significa que naquela subárvore existe 100% de chance de vitória.

Com a lógica de funcionamento já definida, podemos enfim tentar implementar esse algoritmo no nosso jogo.




<a id="implementando-a-abordagem-ingenua"></a>

### Implementando a abordagem ingênua

Como você deve ter notado, o algoritmo precisa sempre gerar as jogadas candidatas a partir de um estado inicial. Sendo assim, esse é um bom ponto de partida para a nossa implementação. Abaixo segue a implementação de uma função para gerar esses candidatos.

```python
from copy import deepcopy

# ...
# FUNÇÔES ANTERIORES FICAM AQUI
# ...


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
```

O que fazemos é, para cada posição livre no tabuleiro, criamos uma cópia desse tabuleiro e ocupamos a próxima posição possível. Com isso criamos uma lista de possíveis movimentos a partir de um estado inicial que foi passado para a função.

Em seguida precisamos de uma função para avaliar os nosso estados finais, ou seja, os estados onde o jogo acabou, seja por vitória, derrota ou empate.

```python
def evaluate(node):
    if is_win(node, CPU_PLAYER):
        return 1

    if is_win(node, HUMAN_PLAYER):
        return -1

    return 0
```

Estamos considerando o **`CPU_PLAYER`** como o **`MAX`** já que precisamos da melhor jogada para ele.

Com essa duas funções definidas já podemos começar a pensar na implementação do nosso Minimax. Como ele é resursivo, quem está familiarizado sabe, que a primeira coisa a ser definida é a condição de parada. No nosso caso verificamos se é um estado final e retornamos a avaliação.

```python
def minimax(board):
    if is_terminal(board):
        return evaluate(board)
```

Para os estados intermediários precisamos saber se está na vez do **`MIN`** ou na vez do **`MAX`**, para tal podemos passar um parâmetro chamado **`maximizing`**, assim saberemos se estamos maximizando ou minimizando. Colocaremos ele como `False` por padrão, apenas por fins de praticidade.

```python
def minimax(board, maximizing=False):
    if is_terminal(board):
        return evaluate(board)
```

Agora precisamos definir o que o algoritmo vai fazer em cada turno. No caso do **`MAX`** temos que analisar as possibilidades e pegar a maior pontuação. A recursividade atrapalha um pouco esse processo já que não temos acesso a pontuação dos outros estados. Uma forma simples de fazer isso seria atribuir o menor valor possível para uma variável e sempre que uma pontuação for maior que ela nós atualizamos esse valor. Dessa forma vamos garantir que no retorno vamos manter sempre a maior prontuação. Essa implementação está ilustrado abaixo.

```python
def minimax(board, maximizing=False):
    if is_terminal(board):
        return evaluate(board)

    if maximizing:
        value = float('-inf')

        for child in candidates(board, CPU_PLAYER):
            value = max(value, minimax(board, False))

    return value
```

Note que quando o valor do **`maximizing`** for **`True`** precisamos passar para a próxima chamada o **`False`** para garantir que todos os turnos serão avaliados corretamente.

Para finalizar só precisamos fazer o mesmo para o **`MIN`**, só que com a lógica contrária, dessa vez vamos iniciar o valor com o número mais alto possível e pegar o mínimo entre as pontuações.

```python
def minimax(board, maximizing=False):
    if is_terminal(board):
        return evaluate(board)

    if maximizing:
        value = float('-inf')

        for child in candidates(board, CPU_PLAYER):
            value = max(value, minimax(child, False))
    else:
        value = float('+inf')

        for child in candidates(board, HUMAN_PLAYER):
            value = min(value, minimax(child, True))

    return value
```


<a id="otimizando-com-a-poda-alfa-beta"></a>

### Otimizando com a poda Alfa-Beta





<a id="aprimorando-ainda-mais-com-heuristicas"></a>

### Aprimorando ainda mais com heurísticas





<a id="recapitulando"></a>

## Recapitulando...


O que fizemos hoje:

- Constuímos o nosso jogo da velha
- Entendemos o que é o Minimax e como ele pode ser utilizado
- Implementamos o Minimax padrão para o jogo
- Vimos que a implementação ingênua do Minimax tem certos problemas
- Implementamos otimizações

Conseguimos fazer o nosso algoritmo super inteligente para jogar o jogo da velha. Vimos que ele tem alguns problemas, mas com a técnica correta eles podem ser contornados. Sinta-se a vontade para procurar outras otimizações e quem sabe aplicar até em outros jogos. Um exercício interessante é pensar quais são os jogos em que ele pode ser aplicado.

Para você que acompanhou esse artigo até o final, muito obrigado pela sua atenção e até o próximo... bye bye
