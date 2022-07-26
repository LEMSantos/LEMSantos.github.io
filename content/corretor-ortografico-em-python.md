Title: Criando um corretor ortográfico simples utilizando Python
Date: 2022-07-23 08:36
Modified: 2022-07-27 08:24
Category: NLP
Tags: Corretor ortográfico, NLP, Python
Slug: corretor-ortografico-em-python
Authors: Lucas Eliaquim
Description: Nesse post vamos construir um corretor ortográfico simples utilizando Python, que apresenta uma boa performance. Esse corretor é baseado na versão desenvolvida pelo Peter Norvig.
Status: draft


![React: JavaScript library](/images/spell-checker-2.jpg)
<p style="text-align: center; margin-top: -27px"><em><a href='https://br.freepik.com/fotos-vetores-gratis/ilustracao'>Ilustração vetor criado por pch.vector - br.freepik.com</a></em></p>


Bom dia, Boa tarde ou Boa noite (dependendo da hora que você está lendo esse artigo), nesse post vamos tentar resolver o problema de criar um corretor ortográfico simples utilizando Python. O conteúdo desse post foi baseado em um atigo criado pelo Peter Norvig em 2007, com o título **[How to Write a Spelling Corrector](https://norvig.com/spell-correct.html){target="_blank"}**. Pensei em falar um pouco sobre isso, porque considero esse assunto muito interessante e acredito que existem outras pessoas que, como eu, pensam o mesmo.

O objetivo desse artigo é ajudar as pessoas que não estão tão familiarizadas com a lingua inglesa, ou mesmo não entenderam muito bem o que o Norvig quis dizer. A minha ideia geral é tentar simplificar o máximo possível a parte estatística e matemática, e quem sabe simplificar um pouco do código.

Como eu faço sempre em meus artigos, segue uma lista de requisitos para ajudar você a aproveitar melhor o conteúdo:

1. O primeiro requisito é ter o interpretador de Python instalado;
2. O segundo é entender o básico da linguagem Python:
    - Variáveis e tipos de dados;
    - Estruturas de condição e repetição;
    - Funções.

Bom, agora que definimos o que precisamos, vamos começar os trabalhos. A primeira coisa que precisamos entender é como esse corretor funciona.


## Vá direto ao assunto...

- [Como o corretor funciona](#como-o-corretor-funciona);
- [A Implementação](#a-implementacao);
    - [Lendo o vocabulário](#vocabulario);
    - [Operações básicas](#operacoes-basicas);
    - [Gerando candidatos](#gerando-candidatos);
    - [Colocando tudo junto](#colocando-tudo-junto).
- [Executando testes](#executando-testes);
- [Sugestões de melhoria](#sugestoes-de-melhoria);
- [Recapitulando](#recapitulando).


<a id="como-o-corretor-funciona"></a>

## Como o corretor funciona


Um corretor ortográfico é uma pessoa ou programa de computador que faz a verificação de um texto ou uma palavra para achar e corrigir erros tipográficos ocasionais.

Na lingua portuguesa, alguns erros comuns podem acontecer quando estamos digitando. Podemos, por exemplo:

- Adicionar uma ou mais letras em uma palavra;
- "Engolir" letras quando estamos digitando;
- Trocar duas ou mais letras de uma palavra;
- Colocar letras que não fazem parte da palavra, como por exemplo, confundir **s** e **z**.

Existem outros erros que podem acontecer, porém vamos nos forcar apenas nesses quatro.

Sendo uma pessoa esperta, acredito que uma certa pergunta pode ter surgido na sua mente: Como fazemos para corrigir esse tipo de erro?

Uma forma bem intuitiva de pensar seria: Podemos gerar todas as palavras possíveis, inserindo, removendo, trocando ou colocando novas letras, e selecionar a palavra que tem a maior chance de ser a correção da palavra original. Muito bem, é exatamente o que vamos fazer. A nossa linha de pensamento pode ser dividida em quatro operações distintas:

- Gerar os possíveis candidatos;
- Definir quais candidatos podem ser uma correção para a nossa palavra;
- Definir a chance de cada candidato;
- Escolher o candidato que tem a maior chance de ser a correção.

**Gerar os possíveis candidatos**: Vamos apenas criar variações da nossa palavra, inserindo, removendo, trocando ou colocando novas letras. Cada variação precisa ser gerada, dado que não sabemos qual é a correta.

**Definir os cadidados plausíveis**: Se pensarmos bem, uma palavra de `N` letras vai ter `N` remoções, `N - 1` trocas entre as letras já existentes, `26N` trocas por novas letras e por fim `26(N - 1)` inserções, totalizando `54N + 25` variações (muitas delas podem ser duplicadas). Para uma palavra de 10 letras, ou seja `N=10`, teríamos 565 variações. Como esse número é grande, talvez uma das formas de reduzir seja eliminando as variações que não fazem parte do nosso vocabulário.

**Definir a chance de cada candidato**: Para definir a chance de cada candidato precisamos saber qual a probabilidade de cada palavra aparecer em um texto. Imagino que você já deve ter pensado nisso, mas uma das formas é pegar um texto, ou vários textos e contar quantas vezes cada palavra aparece. Dessa forma, saberemos qual palavra é mais provável de aparecer.

**Escolher o candidato**: Se já temos os candidatos e a chance de cada candidato de ser a correção para a palavra, só precisamos selecionar aquele que tem a maior chance.

Essas operações compõem as etapas que o nosso corretor precisa executar sempre que a correção de uma nova palavra for solicitada. Agora que definimos toda a linha de prensamento que precisamos, podemos partir para a implementação.

<a id="a-implementacao"></a>

## A implementação

Podemos dividir a nossa implementação em algumas etapas. Essa divisão vai nos ajudar a entender melhor cada parte do nosso corretor. Dentre as fases, temos: a leitura do vocabulário, ou seja, a frenquência das palavras, a criação das operações básicas para gerar os candidatos, gerar de fato os candidatos e por fim, colocar tudo junto para finalizar o corretor.

<a id="vocabulario"></a>

#### Lendo o vocabulário

O nosso vocabulário vai ser basicamente um arquivo `.txt` em que vamos colocar cada palavra e sua respectiva frequência. Para ilustrar, esse arquivo vai estar no formato abaixo:

```txt
que 15044152
não 12169729
o 12005035
de 10121551
a 8992538
é 8594955
você 7817147
e 7345808
```

Esse arquivo que vamos utilizar é uma contagem de palavras gerada a partir do [OpenSubtitles](https://www.opensubtitles.org/pt){target="_blank"}, que é a maior base de dados de legendas em diversas linguas. O arquivo do vocabulário [pode ser encontrado aqui](/docs/vocabulary.txt){target="_blank"}. Vamos chamá-lo de **`vocabulary.txt`**. Você pode conferir também o [aquivo original](https://github.com/hermitdave/FrequencyWords/blob/master/content/2018/pt_br/pt_br_50k.txt) está no github.

Como o nosso arquivo vai ter a palavra e a respectiva frequência separadas por um espaço, podemos modelar o nosso código com os seguintes passos:

- Abrir o arquivo **`vocabulary.txt`**;
- Ler o texto completo e separar cada uma das linhas;
- Para cada linha, separar a palavra da frequência;
- Criar um **`Counter`** para armazenar essas frequências;
- Somar as frequências para saber o total de palavras consideradas. Vamos utilizar isso para calcular a probabilidade de cada palavra;
- Retornar tanto a soma, quanto o **`Counter`**.

O código a seguir ilustra a definição de uma função para realizar essas ações.

```python
from collections import Counter


def read_vocabulary():
    with open('vocabulary.txt') as vocab_file:
        lines = vocab_file.read().splitlines()

    full_vocab = [line.split() for line in lines]
    words_counter = Counter({word: int(count) for word, count in full_vocab})

    return sum(words_counter.values()), words_counter
```

O **`Counter`** é apenas uma estrutura nativa do Python para guardar frequências. É uma estrutura semelhante a um dicionário, onde teremos a palavra como chave e a frequência como valor. Algo como:

```
>>> from collections import Counter
>>> counter = Counter({'que': 15044152})
>>> counter['que']
15044152
```

<a id="operacoes-basicas"></a>

#### Operações básicas

Agora que definimos como será a leitura do nosso vocabulário, vamos partir para as operações básicas de inserção, remoção, troca e substituição. Começameros com a função para criar candidatos a partir de inserção.

```python
LETTERS = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'

# <FUNÇÕES DEFINIDAS ANTERIORMENTE FICAM AQUI>


def generate_by_insert(word):
    generated_words = set()

    for pos in range(len(word) + 1):
        for letter in LETTERS:
            generated_words.add(word[:pos] + letter + word[pos:])

    return generated_words
```

Basicamente a função de gerar candidatos por inserção recebe a palavra como parâmetro e para cada posição inserimos cada uma das letras possíveis. Essa operação divide a palavra em duas partes, lado direito e lado esquerdo. Então ela insere entre as duas partes uma nova letra.

Seguindo, vamos definir a função para gerar candidatos através de remoção.

```python
def generated_by_delete(word):
    generated_words = set()

    for pos in range(len(word) + 1):
        generated_words.add(word[:pos] + word[pos + 1:])

    return generated_words
```

Mesmo esquema da função de inserção, com a diferença de retirar as letras ao invés de inserir. Essa remoção pode ser vista quando descartamos uma das letras da parte direita com o trecho **`word[pos + 1:]`**.

A próxima operação é para gerar candidatos através de substituição.

```python
def generate_by_replace(word):
    generated_words = set()

    for pos in range(len(word) + 1):
        for letter in LETTERS:
            generated_words.add(word[:pos] + letter + word[pos + 1:])

    return generated_words
```

A ideia dessa operação é muito similar a de remoção, com a diferença que ao invés de descartar uma letra, colocamos outra no lugar.

Por último, mas não menos importante, precisamos definir uma função para gerar candidatos através de troca.

```python
def generate_by_swap(word):
    generated_words = set()

    for pos in range(len(word) - 1):
        generated_words.add(
            word[:pos] + word[pos + 1] + word[pos] + word[pos + 2:]
        )

    return generated_words
```

Essa operação simplesmente troca letras dentro da própria palavra, considerando que podem existir erros de digitação onde invertemos a ordem das letras.

Com as operações básicas definidas, podemos finalmente partir para a geração de candidatos.

<a id="gerando-candidatos"></a>

#### Gerando candidatos

Para gerar os candidatos que servirão para corrigir a palavra, precisamos pensar que nem sempre erramos apenas uma vez quando estamos digitando uma palavra. Assim, pode ser que seja necessário criar variações onde um ou mais erros possam ser corridos. Primeiramente vamos resolver o problema de gerar os candidatos para apenas um erro, ou falando de outra forma, com distância igual a 1 em relação a palavra original.

```python
def words_generator_1_dist(word):
    inserts = generate_by_insert(word)
    deletes = generated_by_delete(word)
    replaces = generate_by_replace(word)
    swaps = generate_by_swap(word)

    return inserts | deletes | replaces | swaps
```

Nessa função, simplesmente geramos as variações baseadas em cada uma das operações e depois fazemos a união de todas elas. Assim, teremos um conjunto com todas as palavras com distância igual 1 em relação a palavra passada como parâmetro.

Para resolver o problema da distância igual a 2, ou seja, com a possibilidade de 2 erros sendo cometidos ao mesmo tempo, podemos definir a função como segue:

```python
def words_generator_2_dist(word):
    words_2_dist = set()

    for new_word in words_generator_1_dist(word):
        words_2_dist |= words_generator_1_dist(new_word)

    return words_2_dist
```

Basicamente estamos considerando que, se para cada palavra com distância igual a 1, gerarmos outra palavra com distância igual a 1, conseguimos gerar palavras com distância total igual a 2 em relação a palavra original.

Podemos continuar gerando palavras com mais distâncias para cobrir a maior quantidade possível de erros, porém para cada nova possibilidade que pensamos, a quantidade de palavras aumenta vertiginosamente. Dessa forma, em algum momento podemos não conseguir mais lidar com a quantidade imensa de palavras e acabar eliminando a eficiência do nosso corretor.

Você vai ver que para a grande maioria dos casos, a distância máxima igual a 2 já é o suficiente.

Bom, agora que definimos funções auxiliares para gerar as variações das palavras, podemos enfim selecionar os candidatos mais adequados.

```python
def candidates(misspelled_word):
    return (known_words({misspelled_word}) or
            known_words(words_generator_1_dist(misspelled_word)) or
            known_words(words_generator_2_dist(misspelled_word)) or
            {misspelled_word})
```

Para definir quem é um candidato adequado, precisamos definir um modelo de seleção. Como não temos nenhum banco de erros ortográficos para analisar, podemos pensar em algumas regrinhas simples.

- Se a palavra que foi passada para ser corrigida já existe no nosso vocabulário, então provavelmente ela não precisa ser corrigida. Retornamos ela;
- Ou se, ao gerar variações considerando a distância igual a 1 encontrarmos palavras existentes no vacabulário, então provavelmente elas são os candidatos corretos;
- Ou se, ao gerar variações considerando a distância igual a 2 encontrarmos palavras existentes no vacabulário, então provavelmente elas são os candidatos corretos;
- Se não, retornamos a própria palavra que foi passada, dado que não encontramos correção para ela.

Nesse caso estamos levando em consideração que errar apenas uma vez é mais provável do que errar duas vezes.

Apenas uma coisa faltou, definir a função **`known_words`**, que nos retorna quais palavras de um conjunto estão presentes no nosso vocabulário.

```python
def known_words(words_set):
    vocabulary_words = set(VOCABULARY.keys())
    return words_set & vocabulary_words
```

A variável **`VOCABULARY`** será definida posteriormente.

<a id="colocando-tudo-junto"></a>

#### Colocando tudo junto

Agora que temos todas as funções necessárias para gerar os candidatos para a efetuar a correção, podemos enfim definir a função que de fato faz a correção.

```python
def correct(misspelled_word):
    return max(candidates(misspelled_word), key=probability_of_word)
```

Nesse caso estamos pegando o candidato que apresenta a maior probabilidade de ser a opção correta. Essa probabilidade é basicamente a chance de uma das palavras aparecer baseado na sua frequência. Esse cálculo pode ser feito levando em consideração a quantidade de vezes que a palavra aparece, dividido pela quantidade de palavras consideradas.

A implementação da função de probabilidade pode ser vista abaixo.

```python
def probability_of_word(word):
    return VOCABULARY[word] / TOTAL_WORDS
```

Por fim, vamos fazer a leitura do vocabulário e do total de palavras utilizando a função **`read_vocabulary`** que definimos no início. Depois disso podemos esperar que o usuário insira a palavra, e logo em seguida devolver a correção.

```python
TOTAL_WORDS, VOCABULARY = read_vocabulary()

if __name__ == '__main__':

    misspelled_word = input('Digite a palavra incorreta: ')
    print('Correção:', correct(misspelled_word))
```

Ao rodar o código completo com todas as funções necessárias, vamos ter uma execução igual ao que você pode ver abaixo.

```
Digite a palavra incorreta: lgica
Correção: lógica
```

O código completo do nosso corretor ortográfico [pode ser encontrado aqui](/docs/spell-corrector.py){target="_blank"}. Apenas coloque o arquivo **`vocabulary.txt`** na mesma pasta do arquivo com o código.

<a id="executando-testes"></a>

## Executando testes




<a id="sugestoes-de-melhoria"></a>

## Sugestões de melhoria





<a id="recapitulando"></a>

## Recapitulando...


O que aprendemos hoje:



Para você que acompanhou esse artigo até o final, muito obrigado pela sua atenção e até o próximo... bye bye
