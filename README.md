# Telegram Bot

Olá! Se você chegou até aqui, encontrará neste repositório o código para um bot simples que retorna os 10 primeiros trending topics no Twitter do dia. Desenvolvi esse código com as seguintes ferramentas:

- [python-telegram-bot](https://python-telegram-bot.org/), para consumo da **bot API** **do Telegram.**
- [tweepy](https://www.tweepy.org/), para consumo da **API do Twitter.**
- [Google API Python Client](https://github.com/googleapis/google-api-python-client), para consumo da **YouTube API v3**
- [datetime](https://docs.python.org/3/library/datetime.html#module-datetime), para **formatação de saídas no formato de data.**
- [doten](https://pypi.org/project/python-dotenv/) e [os](https://docs.python.org/3/library/os.html), para gerenciamento das **chaves de API**.

Caso tenha clonado o repositório, você tem em seu repositório um arquivo requirements.txt, com todas as dependências utilizadas nesse projeto, e pode obtê-las de forma rápida para seu ambiente de desenvolvimento com esse comando:

```powershell
pip install -r requirements.txt
```

Para ter acesso às APIs do Telegram e do Twitter, e permitir que o bot funcione, é necessário obter uma **chave de acesso** para cada uma. Você pode obtê-las [aqui (Telegram)](https://t.me/botfather), [aqui (Twitter)](https://developer.twitter.com/en), e [aqui (YouTube)](https://console.cloud.google.com/google/maps-apis/credentials). Uma explicação mais detalhada de como os bots no Telegram funcionam pelo próprio Telegram pode ser encontrada [nesse link](https://core.telegram.org/bots).

As chaves de acesso para a Bot API do Telegram, para a API do Twitter e para a YouTube data API v3, deverão ser substituídas no bot respectivamente **aqui:**

```python
# bot.py
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
from handles import start, echo, unknown
from tt_handles import trends
from yt_handles import video_stats

from dotenv import load_dotenv
import os 

load_dotenv()

TOKEN = os.environ['telegram_token'] # INSIRA AQUI SUA CHAVE DE API
```

**aqui:**

```python
# tt_handles.py
import tweepy
import json
import os

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

BEARER_TOKEN = os.environ['tt_api_bearertoken'] # INSIRA AQUI SUA API TOKEN
```

e aqui:

```python
# yt_handles.py
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ['yt_api_key'] # INSIRA AQUI SUA CHAVE DE API
```

Você pode substituir esses valores diretamente no código, caso queira executar o bort localmente. Se quiser compartlihar o código, o recomendado é criar um arquivo .env com as suas chaves definidas pelo par chave=”valor”, resgatando cada uma no código de acordo com a estrutura acima. Você encontra um exemplo de como esturutrar esse arquivo em .env.example , aqui nesse mesmo repositório.

### ATENÇÃO:

Esse código faz uso do [Twitter API v2.](https://developer.twitter.com/en/docs/api-reference-index) e [OAuth 2.0 Bearer Token (App-Only) authentication handler](https://docs.tweepy.org/en/stable/authentication.html#oauth-2-0-bearer-token-app-only) do Tweepy. É necessário utilizar sua **Bearer Token** para autenticar de forma correta. Seguindo o passo-a-passo corretamente vocês poderão ver o bot em ação sem grandes problemas, podendo inclusive adicionar novas funcionalidades a ele. Façam bom proveito!