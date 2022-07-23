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


Bom dia, Boa tarde ou Boa noite (dependendo da hora que você está lendo esse artigo), nesse post vamos tentar resolver o problema de criar um corretor ortográfico simples utilizando Python. O conteúdo desse post foi baseado em um atigo criado pelo Peter Novig em 2007, com o título **[How to Write a Spelling Corrector](https://norvig.com/spell-correct.html)**. Pensei em falar um pouco sobre isso, porque considero esse assunto muito interessante e acredito que existem outras pessoas que, como eu, pensam o mesmo.

O objetivo desse artigo é ajudar as pessoas que não estão tão familiarizadas com a lingua inglesa, ou mesmo não entenderam muito bem o que o Norvig quis dizer. A minha ideia geral é tentar simplificar o máximo possível a parte estatística e matemática, e quem sabe simplificar um pouco do código.

Como eu faço sempre em meus artigos, segue uma lista de requisitos para ajudar você a aproveitar melhor o conteúdo:

1. O primeiro requisito é ter o interpretador de Python instalado
2. O segundo é entender o básico da linguagem Python:
    - Variáveis e tipos de dados
    - Estruturas de condição e repetição
    - Funções

Bom, agora que definimos o que precisamos, vamos começar os trabalhos. A primeira coisa que precisamos entender é como esse corretor funciona.


## Vá direto ao assunto...

- [Como o corretor funciona](#como-o-corretor-funciona)
- [A Implementação](#a-implementacao)
    - [Lendo o vocabulário](#vocabulario)
    - [Operações básicas](#operacoes-basicas)
    - [Gerando candidatos](#gerando-candidatos)
    - [Colocando tudo junto](#colocando-tudo-junto)
- [Executando testes](#executando-testes)
- [Sugestões de melhoria](#sugestoes-de-melhoria)
- [Recapitulando](#recapitulando)


<a id="como-o-corretor-funciona"></a>

## Como o corretor funciona


Um corretor ortográfico é uma pessoa ou programa de computador que faz a verificação de um texto ou uma palavra para achar e corrigir erros tipográficos ocasionais.

Na lingua portuguesa, alguns erros comuns podem acontecer quando estamos digitando. Podemos, por exemplo:

- Adicionar uma ou mais letra em uma palavra
- "Engolir" uma letra quando estamos digitando
- Trocar duas ou mais letras de uma palavra
- Colocar letras que não fazem parte da palavra, como por exemplo, confundir **s** e **z**.

Existem outros erros que podem acontecer, porém vamos nos forcar apenas nesses quatro.

Sendo uma pessoa esperta, acredito que uma certa pergunta pode ter surgido na sua mente: Como fazemos para corrigir esse tipo de erro?

Uma forma bem intuitiva de pensar seria: Podemos gerar todas as palavras possíveis, inserindo, removendo, trocando ou colocando novas letras, e selecionar a palavra que tem a maior chance de ser a correção da palavra original. Muito bem, é exatamente o que vamos fazer. A nossa linha de pensamento pode ser dividida em quatro operações distintas:

- Gerar os possíveis candidatos
- Definir quais candidatos podem ser uma correção para a nossa palavra
- Definir a chance de cada candidato
- Escolher o candidato que tem a maior chance de ser a correção

**Gerar os possíveis candidatos**: Vamos apenas criar variações da nossa palavra, inserindo, removendo, trocando ou colocando novas letras. Cada variação precisa ser gerada, dado que não sabemos qual é a correta.

**Definir os cadidados plausíveis**: Se pensarmos bem, uma palavra de `N` letras vai ter `N` remoções, `N - 1` trocas entre as letras já existentes, `26N` trocas por novas letras e por fim `26(N - 1)` inserções, totalizando `54N + 25` variações (muitas delas podem ser duplicadas). Para uma palavra de 10 letras, ou seja `N=10`, teríamos 565 variações. Como esse número é grande, talvez uma das formas de reduzir seja eliminando as variações que não fazem parte do nosso vocabulário.

**Definir a chance de cada candidato**: Para definir a chance de cada candidato precisamos saber qual a probabilidade de cada palavra aparecer em um texto. Imagino que você já deve ter pensado nisso, mas uma das formas é pegar um texto, ou vários textos e contar quantas vezes cada palavra aparece. Dessa forma, saberemos qual palavra é mais provável de aparecer.

**Escolher o candidato**: Se já temos os candidatos e a chance de cada candidato de ser a correção para a palavra, só precisamos selecionar aquele que tem a maior chance.



<a id="a-implementacao"></a>

## A implementação





<a id="executando-testes"></a>

## Executando testes




<a id="sugestoes-de-melhoria"></a>

## Sugestões de melhoria





<a id="recapitulando"></a>

## Recapitulando...


O que aprendemos hoje:

- O que são chatbots e os seus tipos;
- Definimos os pacotes que vamos utilizar para desenvolver o nosso software;
- Definimos a organização do nosso projeto.

No próximo artigo vamos de fato desenvolver o nosso chatbot e torna-lo funcional.

Para você que acompanhou esse artigo até o final, muito obrigado pela sua atenção e até o próximo... bye bye
