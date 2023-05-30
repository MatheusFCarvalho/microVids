import os
import cv2
from moviepy.editor import ImageSequenceClip, concatenate_videoclips
from moviepy.audio import AudioFileClip

def criar_video():
    pasta = os.getcwd()  # Obter o diretório atual
    imagens = []
    
    # Percorrer a pasta em busca de arquivos de imagem
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
            caminho = os.path.join(pasta, arquivo)
            imagem = cv2.imread(caminho)  # Carregar a imagem usando o OpenCV
            imagens.append(imagem)
    
    # Criar o vídeo com as imagens
    video = ImageSequenceClip(imagens, fps=0.5)  # 0.5 frames por segundo (2 segundos por imagem)
    video = video.resize((1080, 1080))  # Redimensionar para 1080x1080 pixels
    
    # Adicionar música ao vídeo
    musica = os.path.join(pasta, "musica.mp3")  # Caminho do arquivo de música
    clip_musica = AudioFileClip(musica)
    video_com_audio = video.set_audio(clip_musica)
    
    # Salvar o vídeo com música como arquivo .mp4
    video_com_audio.write_videofile("output.mp4", codec="libx264", fps=24)

criar_video()
