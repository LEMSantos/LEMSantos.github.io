Title: Primeiro chatbot em Python - Parte 1: Planejamento
Date: 2022-06-23 08:36
Modified: 2022-06-27 08:24
Category: Chatbot
Tags: Chatterbot, Telegram, Python, Chatbot
Slug: primeiro-chatbot-em-python-parte-1
Authors: Lucas Eliaquim
Description: Nesse artigo vamos iniciar o projeto para a construção do nosso chatbot, e para isso precisamos entender melhor o que é um chatbot e quais tipos existem, além de realizar o planejamento da nossa implementação.
Status: published


![React: JavaScript library](/images/chatbot-banner.webp)
<p style="text-align: center; margin-top: -27px"><em><a href="https://br.freepik.com/fotos-vetores-gratis/chatbot">Chatbot vetor criado por pch.vector - br.freepik.com</a></em></p>


Bom dia, Boa tarde ou Boa noite (dependendo da hora que você está lendo esse artigo), nesta série, vamos construir o nosso chatbot utilizando a linguagem **Python**. O nosso projeto, vai desde o planejamento até o ponto em que ele esteja respondendo para os nossos usuários, ou para nós mesmos, porque não?!

Antes de iniciarmos a nossa jornada, é interessante que você, meu querido leitor, minha querida leitora, cumpra alguns requisitos básicos para que o seu aprendizado seja satisfatório, são eles:

1. Ter o interpretador de Python instalado no seu computador (**Importante!!**)
2. Ter um conhecimento básico da linguagem python:
    - Variáveis e tipos de dados
    - Estruturas de condições e repetição
    - Funções
    - Como instalar e utilizar bibliotecas

**Obs: Para tudo o que eu fiz ou fizer nos proximos artigos, eu utilizei/utilizarei o sistema operacional Ubuntu, mas não se sinta desencorajado por causa disso, caso você seja usuário de Mac ou Windows, todos os códigos funcionarão perfeitamente nestes outros sistemas operacionais.**

Esses requisitos citados acima são os mais básicos que precisamos para desenvolver o nosso projeto, a medida que o projeto avança, caso seja necessário que você possua mais algum tipo de conhecimento específico eu avisarei, com toda a certeza, ai caso você não entenda muito sobre o tópico, eu também colocarei algumas referências para facilitar o entendimento.

Com tudo certo para dar errado (hehehehehe) vamos iniciar o nosso projeto. Antes de mais nada é importante saber **o que é um chatbot**, quais os tipos, o que fazem, como vivem, o que comem...


## Chatbots fantásticos e onde habitam


O chatbots são existências interessantes; mágicos para alguns, intrigantes para outros e até mesmo irritantes às vezes (Quantas vezes já falamos com uma central de atendimento, muito irritados, e nos deparamos com uma máquina "burra"?). Eles, no entanto, **não são magia**, apenas **tecnologia**.

Podemos encontrar muitas definições formais para o que seria um chatbot, mas gostaria de destacar uma delas para você:


>_Um chatbot é um software capaz de manter uma conversa com um usuário humano em linguagem natural, por meio de aplicativos de mensagens, sites, e outras plataformas digitais. Eles são sistemas que usam uma interface conversacional para entregar um produto, serviço ou experiência._

<br>


Apesar dessa definição estar particularmente boa, geralmente elas não são. Mas para resumir, um chatbot é um **software/agente/programa**, como queira chamar, que simula uma conversa humana, de preferência de uma forma que o ser humano que conversa com ele não consiga saber se está falando com uma máquina ou não (Ainda está difícil).

Podemos encontrar muitos tipos de chatbots no mercado, mas para simplificar vou citar apenas dois: O chatbot baseado em regras e o chatbot baseado em Inteligência Artificial.

#### Chatbot baseado em regras

Os chatbots baseados em regras só aceitam **um número definido de solicitações** e tem um **vocabulário muito limitado**, geralmente utilizam botões para restringir as respostas do usuário, mas mesmo tão limitados, eles conseguem resolver uma gama muito grande de problemas, e com sua simplicidade de implementação, acabam se tornando uma opção viável para muitas pessoas.

#### Chatbot baseado em Inteligência Artificial

Os chatbots baseados em IA geralmente são bem mais inteligentes e conseguem "entender" as intenções do usuário, conseguindo assim, tornar o chat mais dinâmico e talvez mais agradável. A sua complexidade de construção aumenta significativamente e isso talvez seja uma desvantagem de utilizar esse tipo de abordadem.

Mas chega de falatório, porque com certeza você não chegou até aqui para aprender somente conceitos, então vamos para o nosso planejamento.


## Requirements do projeto


Como você garantiu que atendeu os meus requisitos iniciais, acredito que já esteja familiarizado com o `pip`, o gerenciador de pacotes do python, caso não esteja não se preocupe, esse [artigo](https://realpython.com/what-is-pip/) pode te ajudar. Os pacotes necessários que serão utilizados encontram-se logo abaixo:

```bash
# requirements.txt

ChatterBot
chatterbot-corpus
telepot
```

Todos eles podem ser instalados individualmente, mas para uma maior praticidade, podemos colocar todos em um arquivo `requirements.txt` e executar o comando abaixo para instalar todos de uma só vez

```bash
$ pip install -r requirements.txt
```

**Não se preocupe ainda com os pacotes que vamos utilizar, a medida que eles forem necessários, eu explicarei em detalhes o seu funcionamento.**


## Estrutura do projeto


Quem trabalha com programação há um pouco mais de tempo, já deve ter notado que para uma projeto bem sucedido uma estrutura de organização é de extrema importância e pode facilitar ou dificultar o desenvolvimento. No nosso caso, como o projeto é relativamente simples, a nossa estrutura também será.

```
.
├── chatbot.py
├── data
├── main.py
└── requirements.txt
```

A pasta **`data`** servirá para colocarmos os dados de treinamento do chatbot (não se preocupe com isso no momento), o arquivo **`chatbot.py`** será aquele em que vamos definir o nosso chatbot e como ele vai se comportar, temos ainda o arquivo **`requirements.txt`** que já foi citado acima, e por último, mas não menos importante o arquivo **`main.py`** que será o arquivo principal do nosso programa e nele vamos definir tudo o que precisamos para que o chatbot consiga dar as respostas para as solicitações.


## Pacotes que serão utilizados


Para desenvolver a nossa aplicação, além dos pacotes da biblioteca padrão do Python, vamos precisar de 2 pacotes adicionais, são eles:

#### Chatterbot

Chatterbot é uma biblioteca que torna mais fácil gerar respostas automatizadas para as solicitações do usuário. Ela utiliza uma seleção de algoritmos de Machine Learning para produzir diferentes tipos de respostas. Isto facilita para os desenvolvedores criarem chatbots e automatizar conversas com o usuário. Caso tenha interesse em estudar em mais detalhes essa biblioteca, segue o link para a [documentação](https://chatterbot.readthedocs.io/en/stable/).

Um exemplo de interação mecionado na própria documentação seria:

```text
user: Good morning! How are you doing?
bot:  I am doing very well, thank you for asking.
user: You're welcome.
bot:  Do you like hats?
```

#### Telepot

Telepot é uma biblioteca que ajuda os desenvolvedores a construir softwares para se comunicar com a [API de bots do Telegram](https://core.telegram.org/bots). Ela possui versões que funcionam tanto com o Python 2.7, quanto com o Python 3. Segundo a própria [documentação](https://telepot.readthedocs.io/en/latest/) da biblioteca a melhor forma de entender o seu funcionamente é lendo a parte principal da mesma e olhando para os [exemplos](https://github.com/nickoala/telepot/tree/master/examples).


## Recapitulando...


O que aprendemos hoje:

- O que são chatbots e os seus tipos;
- Definimos os pacotes que vamos utilizar para desenvolver o nosso software;
- Definimos a organização do nosso projeto.

No próximo artigo vamos de fato desenvolver o nosso chatbot e torna-lo funcional.

Para você que acompanhou esse artigo até o final, muito obrigado pela sua atenção e até o próximo... bye bye
