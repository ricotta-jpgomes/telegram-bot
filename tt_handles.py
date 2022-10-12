# HANDLES DE INTEGRAÇÃO COM OS SERVIÇOS DO TWITTER
import tweepy
import json
import os

from dotenv import load_dotenv
from datetime import datetime

# RESGATANDO MINHAS CHAVES DE API DO ARQUIVO MEU .env:
load_dotenv()

# CHAVES DE ACESSO À API (OBTENHA AS SUAS AQUI: https://developer.twitter.com/en/docs/twitter-api)
'''
API_KEY = os.environ['tt_api_key']
API_SECRET = os.environ['tt_api_key_secret']
ACCESS_TOKEN = os.environ['tt_api_accesstoken']
ACCESS_TOKEN_SECRET = os.environ['tt_api_accesstoken_secret']
'''
BEARER_TOKEN = os.environ['tt_api_bearertoken']
BRAZIL_WOE_ID = 23424768
 
def trends(update, context, token=BEARER_TOKEN):
   # REALIZANDO AUTENTICAÇÃO NA API COM AS MINHAS CHAVES DE ACESSO
   auth = tweepy.OAuth2BearerHandler(token)

   api = tweepy.API(auth)
   # OBTENDO OS TRENDING TOPICS DO BRASIL ATRAVÉS DE SEU 'WHERE ON EARTH IDENTIFIER'
   response = api.get_place_trends(BRAZIL_WOE_ID) 
   trends = json.loads(json.dumps(response)) # TRANSFORMANDO O RETORNO DA REQUISIÇÃO PARA UMA ESTRUTURA DE DADOS
   # OS DADOS RETORNAM COMO UMA LISTA DE DICIONARIOS.
   # AS INFORMAÇÕES QUE EU PRETENDO EXIBIR NO FINAL SERÃO ARMAZENADAS NA VARIAVEL ABAIXO - output_list:
   output_list = []
   # AGORA, REALIZAMOS UM FOR LOOP ARMAZENANDO AS INFORMAÇÕES QUE SERÃO EXIBIDAS NA MENSAGEM EM UM NOVO DICIONARIO.
   # NO CASO, PRETENDO EXIBIR APENAS O NOME DO TOPICO E UM LINK PARA OS TWEETS RELATIVOS AQUELE TÓPICO 
   for i in range(0,10): # A PRINCÍPIO, QUEREMOS APENAS OS DEZ PRIMEIROS TÓPICOS DO TOTAL. 
      final_trend = {}

      trend_name = trends[0]['trends'][i]['name'] # NOME DO TÓPICO
      trend_url = trends[0]['trends'][i]['url'] # URL PARA OS TWEETS RELATIVOS AO TÓPICO
      # ARMAZENANDO OS VALORES NO DICIONÁRIO FINAL
      final_trend['name'] = trend_name
      final_trend['link'] = trend_url
      # GUARDANDO O DICIONÁRIO NA LISTA DE SAÍDA
      output_list.append(final_trend)
   # AQUI OBTEMOS E FORMATAMOS O DIA PARA EXIBIR NO CABEÇALHO DA MENSAGEM FINAL
   today = datetime.now().strftime("%d/%m/%Y")   
   # FORMATANDO O TEXTO QUE SERÁ EXIBIDO NA MENSAGEM
   text = (
            f'TRENDING TOPICS NO BRASIL EM {today}\n\n\n'
            f'1. {output_list[0]["name"]}\n'
            f'Link: {output_list[0]["link"]}\n\n'
            f'2. {output_list[1]["name"]}\n'
            f'Link: {output_list[1]["link"]}\n\n'
            f'3. {output_list[2]["name"]}\n'
            f'Link: {output_list[2]["link"]}\n\n'
            f'4. {output_list[3]["name"]}\n'
            f'Link: {output_list[3]["link"]}\n\n'
            f'5. {output_list[4]["name"]}\n'
            f'Link: {output_list[4]["link"]}\n\n'
            f'6. {output_list[5]["name"]}\n'
            f'Link: {output_list[5]["link"]}\n\n'
            f'7. {output_list[6]["name"]}\n'
            f'Link: {output_list[6]["link"]}\n\n'
            f'8. {output_list[7]["name"]}\n'
            f'Link: {output_list[7]["link"]}\n\n'
            f'9. {output_list[8]["name"]}\n'
            f'Link: {output_list[8]["link"]}\n\n'
            f'10. {output_list[9]["name"]}\n'
            f'Link: {output_list[9]["link"]}\n\n'
   )
   # ENVIANDO A MENSAGEM FINAL COM OS TRENDING TOPICS PARA O USUÁRIO
   context.bot.send_message(chat_id=update.effective_chat.id, text=text)