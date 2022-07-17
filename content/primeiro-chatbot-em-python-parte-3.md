Title: Primeiro chatbot em Python - Parte 3: Provisionamento
Date: 2022-07-15 14:06
Modified: 2022-07-15 14:06
Category: NLP
Tags: Chatterbot, Telegram, Python, Chatbot
Slug: primeiro-chatbot-em-python-parte-3
Authors: Lucas Eliaquim
Description: Chegamos a última parte do nosso projeto de construção do primeiro chatbot em Python. Agora vamos finalmente construir uma estrutura que nos permita compartilhar ele com o mundo.
Status: draft


![React: JavaScript library](/images/telegram-banner.webp)
<p style="text-align: center; margin-top: -27px"><em><a href="https://br.freepik.com/fotos-vetores-gratis/chatbot" target="_blank">Chatbot vetor criado por pch.vector - br.freepik.com</a></em></p>

Bom dia, Boa tarde ou Boa noite (dependendo da hora que você está lendo esse artigo), vamos, em fim, terminar o projeto que começamos na [Parte 1](/primeiro-chatbot-em-python-parte-1.html) e na [Parte 2](/primeiro-chatbot-em-python-parte-2.html) dessa série. Depois do planejamento que fizemos e da implementação efetiva do nosso chatbot, temos que mostrá-lo ao mundo, ou quem sabe só a parentes próximos (hehehe). Para tal, vamos utilizar o Telegram, dado que permite disponibilizar os nossos bots gratuitamente.

Antes de iniciarmos a implementação, é interessante nos aprofundar um pouco mais em como a biblioteca Telepot pode nos ajudar a realizar essa conexão entre o nosso código em Python e o Telegram.

## Telepot

Sobre a biblioteca telepot, não temos muito o que dizer. Apenas para resumir, ela é um forma de construir uma comunicação com a [API de bots do Telegram](https://core.telegram.org/bots). Essa biblioteca funciona tanto com Python 2.7 e Python 3, além de que para Python 3.5+ ela ainda disponibiliza a possibilidade de versões de comunicação assíncrona.

De acordo com o próprio autor da [documentação](https://telepot.readthedocs.io/en/latest/) seria complicado listar todas as features que a bilbioteca oferece, então ele desistiu (hehehe). Assim, a melhor forma de entender como ela funciona seria ler a primeira página de introdução e depois conferir todos os exemplos que são listados.

O motivo para utilizarmos essa biblioteca é que ela facilita o nosso trabalho, além de ser bem simples de entender, e com poucas linhas já conseguiremos resolver o nosso problema.

Dito isto, sigamos para a nossa tão esperada implementação...

## Implementação

Bom, antes de qualquer coisa é importante criar um bot no telegram, para que possamos conectar com ele. Está fora do escopo desse artigo como você pode fazer isso, mas acredito que esse [artigo](https://tecnoblog.net/responde/como-criar-um-bot-no-telegram/) pode ajudar.

Nesse ponto, vou assumir que você já passou pelos artigos anteriores e já conseguiu deixar o chatbot funcional. A partir de agora vamos trabalhar apenas no arquivo **`main.py`**.

Como sempre para as pessoas mais apressadinhas segue o código final. Você pode testá-lo, e qualquer problema deixe nos comentários que vamos resolver o mais rápido possível. Mesmo depois de testar é importante que você veja também a explicação passo a passo para que o aprendizado seja melhor fixado.

```python
# Arquivo: main.py

import time

import telepot
from telepot.loop import MessageLoop

from chatbot import chatbot

bot = telepot.Bot('<TOKEN-BOLADÃO-DO-TELEGRAM>')


def handle_telegram_message(message):
    content_type, _, chat_id = telepot.glance(message)

    if content_type == 'text':
        chatbot_response = str(chatbot.get_response(message.get('text')))
        bot.sendMessage(chat_id, chatbot_response)


if __name__ == '__main__':
    MessageLoop(bot, handle_telegram_message).run_as_thread()
    print('Escutando mensagens do Telegram...')

    while True:
        time.sleep(10)
```

A primeira coisa que precisamos fazer são as importações. De início precisamos da biblioteca **`time`**, que já vem no core do Python.

```python
import time
```

Essa bilbioteca vai nos ajudar a manter o nosso programa rodando já que a comunicação com o telegram será feita de forma assíncrona. Logo em seguida fazemos as importações necessárias da bilbioteca **`telepot`**.

```python
import telepot
from telepot.loop import MessageLoop
```

E por fim, temos que importar o chatbot que criamos na parte 2 dessa série com o seguinte trecho de código:

```python
from chatbot import chatbot
```

Em seguida precisamos criar a conexão entre o Telegram e o nosso código. A biblioteca telepot nos ajuda com isso.
Precisamos apenas instânciar o nosso bot passando o **token** que pegamos ao utilizar o botfather. Isso pode ser exemplificado com o trecho de código:

```python
bot = telepot.Bot('<TOKEN-BOLADÃO-DO-TELEGRAM>')
```

Ai precisamos só substituir **`<TOKEN-BOLADÃO-DO-TELEGRAM>`** pelo token correto e a conexão já será estabelecida. Não esqueça o token é secreto e não pode ser repassado.

Seguindo, agora é hora de definir como o nosso bot vai se comportar quando alguém mandar uma mensagem para ele. Podemos fazer isso definindo uma função.

```python
def handle_telegram_message(message):
    content_type, _, chat_id = telepot.glance(message)

    if content_type == 'text':
        chatbot_response = str(chatbot.get_response(message.get('text')))
        bot.sendMessage(chat_id, chatbot_response)
```

Essa função será chamada todas as vezes que uma mensagem nova chegar. Basicamente precisamos recuperar da mensagem o tipo da mensagem enviada (**`content_type`**), e o id de quem enviou a mensagem (**`chat_id`**). Precisamos saber o tipo da mensagem para filtrar caso venha algo diferente de texto, dado que o nosso bot não está preparado para responder. O id serve para que possamos encaminhar a resposta para a pessoa correta.

Logo em seguida temos a última parte do nosso código.

```python
if __name__ == '__main__':
    MessageLoop(bot, handle_telegram_message).run_as_thread()
    print('Escutando mensagens do Telegram...')

    while True:
        time.sleep(10)
```

Nessa etapa vamos definir o loop de mensagem para rodar cada vez que uma nova mensagem chega. Como esse loop roda de forma assíncrona, caso deixássemos sem mais nenhum trecho de código, o programa simplesmente finalizaria e o nosso bot não poderia responder. Por isso, deixamos o loop infinito.

```python
while True:
    time.sleep(10)
```

Ele vai garantir que o nosso programa não será finalizado.

Com tudo definido, você já pode rodar o código e falar com o seu bot através do telegram.

![Exemplo de conversa no Telegram](/images/telegram-example.jpeg){height=500px}

## Recapitulando...


O que fizemos hoje:

- Criamos o nosso bot no telegram
- Implementamos a conexão do nosso chatbot com a interface do telegram
- Finalizamos o nosso projeto :)

Finalmente o nosso chatbot está no ar respondendo através do telegram. E agora, fica por sua conta construir o conhecimento do seu bot. Divirta-se conversando com ele e quem sabe melhorando o projeto para que o bot fique cada vez mais inteligente.

Para você que acompanhou esse artigo até o final, muito obrigado pela sua atenção e até o próximo... bye bye
