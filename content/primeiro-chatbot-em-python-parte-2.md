Title: Primeiro chatbot em Python - Parte 2: Implementação
Date: 2022-06-20 19:00
Modified: 2022-06-20 19:00
Category: Python
Tags: Chatterbot, Telegram, Python, Chatbot
Slug: primeiro-chatbot-em-python-parte-2
Authors: Lucas Eliaquim
Summary: Artigo sobre a criação de um chatbot utilizando python com a biblioteca Chatterbot e deploy com o Telegram.
Status: draft


<a href="https://br.freepik.com/fotos-vetores-gratis/fundo">Fundo vetor criado por pch.vector - br.freepik.com</a>

![React: JavaScript library](/images/coding-banner.jpg)


Bom dia, Boa tarde ou Boa noite, voltamos para continuar a empreitada que começamos no [artigo anterior](/drafts/primeiro-chatbot-em-python-parte-1.html), de construir o nosso primeiro chatbot com python. Dessa vez vamos realmente implementar o nosso chatbot e testa-lo com a base de conhecimento que vamos construir.

Antes de iniciarmos a implementação, é interessante nos aprofundar um pouco mais em como a biblioteca Chatterbot vai nos ajudar a desenvolver o nosso bot.

## Chatterbot

Chatterbot é uma biblioteca que torna mais fácil gerar respostas automatizadas para as solicitações do usuário. Ela utiliza uma seleção de algoritmos de Machine Learning para produzir diferentes tipos de respostas. Isto facilita para os desenvolvedores criarem chatbots e automatizar conversas com o usuário.

## Implementação

Bom, depois de toda essa teoria estamos prontos para realizar a nossa implementação. Vamos nos concentrar inteiramente no arquivo **`chatbot.py`**, nele vamos implementar toda a lógica de treinamento para o nosso bot, e por fim, construir um mecanismo para que possamos testar o seu funcionamento antes de disponibiliza-lo para os usuários.

Para aqueles que são mais apressados, o código final do nosso bot seria algo como:

```python
# Arquivo: chatbot.py

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Jarvis', read_only=True)
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    'chatterbot.corpus.portuguese',
    './data',
)

if __name__ == '__main__':
    while True:
        try:
            user_input = input('Usuário: ')
            bot_response = chatbot.get_response(user_input)

            print('Chatbot:', bot_response)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

```

A partir de agora vamos verificar, parte por parte da implementação e entender como o bot está funcionando e como podemos testa-lo.

Antes de mais nada, precisamos importar as bibliotecas que vamos utilziar para começar o nosso código:

```python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
```

Importamos tanto o **`ChatBot`**, responsável por criar a instância do nosso bot, para que possamos treinar e gerar as respostas para as solicitações do usuário, quanto o **`ChatterBotCorpusTrainer`** que é responsável por criar o mecanismo que vamos utilizar para treinar o nosso bot, com os arquivos que vamos definir.

Após as importações, podemos enfim, criar o nosso chatbot com um nome extremamente original (kkkkkk).

```python
chatbot = ChatBot('Jarvis', read_only=True)
```

A opção **`read_only=True`** foi utilizada para garantir que o nosso bot aprenderá apenas o que nós vamos ensinar a ele, e vai descartar como possibilidade de aprendizado as respostas que o usuário vai inserir.

O treinamento está a cargo do nosso **`trainer`**, que é responsável por gerar o conhecimento do nosso bot, para que ele possa selecionar a melhor resposta, de acordo com o que ele aprendeu, para oferecer de acordo com a solicitação do usuário.

```python
trainer = ChatterBotCorpusTrainer(chatbot)
```

O nosso **`trainer`** é do tipo **`ChatterBotCorpusTrainer`**, que basicamente vai permitir que possamos definir o conhecimento que queremos passar para o nosso bot a partir de arquivos com a extensão `.yml`, que vão ter um formato específico, que mais a frente eu detalharei.

Em seguida podemos finalmente treinar o nosso bot com o trecho de código:

```python
trainer.train(
    'chatterbot.corpus.portuguese',
    './data',
)
```

Em resumo, temos duas linhas importantes que precisamos detalhar: `'chatterbot.corpus.portuguese'` e `'./data'`. A primeira linha diz respeito, a utilização de dados padrão que a biblioteca nos disponibiliza, esses dados estão em português e podemos utilizar para obter as primeiras respostas do nosso bot e testar o seu funcionamento. Essa primeira linha pode ser removida posteriormente quando você tiver construido um banco de conhecimento interessante.

A segunda linha `'./data'` especifica o caminho para a nossa pasta onde colocaremos os nosso arquivos para treinamento, esse caminho não precisa necessariamente ser esse, ele pode ser qualquer caminho válido no seu computador.

Por último, mas não menos importante, chegamos a última parte do nosso código:

```python
if __name__ == '__main__':
    while True:
        try:
            user_input = input('Usuário: ')
            bot_response = chatbot.get_response(user_input)

            print('Chatbot:', bot_response)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
```

Com esse trecho, adicionamos efetivamente a possibilidade de testar a nossa implementação do chatbot. Basicamente ele define um loop infinito para receber as entradas do usuário a partir do console. Esse loop será quebrado quando o usuário inserir `CTRL + C` ou `CTRL + D`, finalizando o programa. Dentro, estamos recebendo a solicitação do usuário através da entrada padrão e devolvendo a resposta que o bot gera com o trecho:

```python
bot_response = chatbot.get_response(user_input)
```

Pronto, finalizamos a implementação do nosso bot, podemos agora executar o código utilizando o comando:

```bash
$ python chatbot.py
```

A execução, seria algo parecido com:

```console
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /home/sysvale/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
[nltk_data] Downloading package stopwords to
[nltk_data]     /home/sysvale/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
/home/sysvale/Área de Trabalho/Personal/chatbot-com-python/.venv/lib/python3.8/site-packages/chatterbot/corpus.py:38: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
  return yaml.load(data_file)
Training compliment.yml: [####################] 100%
Training conversations.yml: [####################] 100%
Training greetings.yml: [####################] 100%
Training linguistic_knowledge.yml: [####################] 100%
Training proverbs.yml: [####################] 100%
Training suggestions.yml: [####################] 100%
Training trivia.yml: [####################] 100%
Training unilab.yml: [####################] 100%
Usuário:
```

O console fica esperando a entrada do usuário para gerar uma resposta do bot.

Com tudo lindo e bonito, precisamos escrever os arquivos que vão compor o banco de conhecimento do nosso bot. Esses aquivos tem um formato simples:

```yaml
# Arquivo: general.yml ou general.yaml

categories:
- geral
conversations:
- - Bom Dia como você está?
  - Eu estou bem, e você?
  - Eu também estou.
  - Que bom.
  - Sim.
- - Olá, tá tudo bem com você?
  - Está tudo bem, obrigado por perguntar.
```

Podemos definir categorias para as conversas e cada uma delas é definida a partir do marcador `- -` e segue o fluxo. Cada conversa deve ter uma sequencia lógica para que o bot saiba a sequencia em que ele deve utilizar a base de conhecimento.

Com tudo finalizado, você pode agora se divertir criando o seu banco de conhecimento, separado em um ou mais arquivos, com uma ou mais categorias, e por fim, tentar conversar com ele para saber como ele responde.

## Recaptulando...


O que fizemos hoje:

- Implementamos o nosso chatbot
- Criamos arquivos de treinamento para o nosso bot
- Testamos o funcionamento

No próximo artigo vamos ver como podemos disponibilizar o chatbot através do telegram e finalizar a nossa construção do nosso primeiro chatbot em python.

Para você que acompanhou esse artigo até o final, muito obrigado pela sua atenção e até o próximo... bye bye