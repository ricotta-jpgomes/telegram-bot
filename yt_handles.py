# HANDLES DE INTEGRAÇÃO COM OS SERVIÇOS DO YOUTUBE
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# RESGATANDO MINHAS CHAVES DE API DO ARQUIVO.env:
load_dotenv()
# CHAVE DE ACESSO À API (OBTENHA A SUA AQUI: )
API_KEY = os.environ['yt_api_key']

def get_video_id(video_link):
    sliced_link = video_link[:-12:-1]
    
    return sliced_link[::-1]

def video_stats(update, context, key=API_KEY):

    youtube = build('youtube','v3', developerKey=key) # INICIALIZANDO MEU CLIENTE 
    video_id = get_video_id(update.message.text) # EXTRAINDO O ID PELO LINK DO VÍDEO ENVIADO NO CHAT
    
    res = youtube.videos().list(part='statistics,snippet', id=video_id).execute()
    data = res['items'][0]

    title = data['snippet']['title']
    channel = data['snippet']['channelTitle']
    views = data['statistics']['viewCount']
    likes = data['statistics']['likeCount']
    comments = data['statistics']['commentCount']

    text = (
        f'ESTATÍSTICAS PARA O VÍDEO {video_id}\n'
        f'Título: {title}\n\n'
        f'Visualizações: {views}\n'
        f'Likes: {likes}\n'
        f'Comentários: {comments}\n\n'
        f'Publicado por: {channel}' 
    )
    # ENVIANDO A MENSAGEM FINAL COM AS ESTATÍSTICAS DO VÍDEO PARA O USUÁRIO
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)



