# Telegram Multi Bot

Olá! Se você chegou até aqui, encontrará neste repositório o código para um bot simples que retorna os 10 primeiros trending topics no Twitter do dia ou as estatísticas de um vídeo do YouTube a partir do seu link. Desenvolvi esse código com as seguintes ferramentas:

- [python-telegram-bot](https://python-telegram-bot.org/), para consumo da **bot API** **do Telegram.**
- [tweepy](https://www.tweepy.org/), para consumo da **API do Twitter.**
- [Google API Python Client](https://github.com/googleapis/google-api-python-client), para consumo da **YouTube API v3**
- [datetime](https://docs.python.org/3/library/datetime.html#module-datetime), para **formatação de saídas no formato de data.**
- [dotenv](https://pypi.org/project/python-dotenv/) e [os](https://docs.python.org/3/library/os.html), para gerenciamento das **chaves de API**.

Caso tenha clonado o repositório, você tem em seu repositório um arquivo requirements.txt, com todas as dependências utilizadas nesse projeto, e pode obtê-las de forma rápida para seu ambiente de desenvolvimento com esse comando:

```powershell
pip install -r requirements.txt
```

Para ter acesso às APIs do Telegram e do Twitter, e permitir que o bot funcione, é necessário obter uma **chave de acesso** para cada uma. Você pode obtê-las [aqui (Telegram)](https://t.me/botfather), e [aqui (Twitter)](https://developer.twitter.com/en). Para uma explicação mais detalhada de como os bots no Telegram funcionam, pode acessar [esse link](https://core.telegram.org/bots).

As chaves de acesso para a Bot API do Telegram, para a API do Twitter, e para a API do Youtube deverão ser substituídas no bot respectivamente **aqui:**

```python
# bot.py
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
from handles import start, echo, unknown
from tt_handles import trends

TOKEN = '' # Chave de acesso a Telegram Bot API.
```

E **aqui:**

```python
import tweepy
import json
import os

from dotenv import load_dotenv
from datetime import datetime

# RESGATANDO MINHAS CHAVES DE API DO ARQUIVO .env:
load_dotenv()
# TOKEN DE ACESSO À API (OBTENHA O SEU AQUI: https://developer.twitter.com/en/docs/twitter-api)
BEARER_TOKEN = os.environ['tt_api_bearertoken']
```

Seguindo esse passo-a-passo vocês poderão ver o bot em ação sem grandes problemas, podendo inclusive adicionar novas funcionalidades a ele. Façam bom proveito!
