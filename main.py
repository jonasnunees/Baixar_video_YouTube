from pytube import YouTube
from pathlib import Path
import os
from pywebio.input import *
from pywebio.output import *


def video_download():
    while True:
        video_link = input('Link do YouTube')
        if video_link.split("//")[0] == "https:":
            put_text('Fazendo download...'.title()).style('color: red; font-size: 50px')
            video_url = YouTube(video_link)
            video = video_url.streams.get_highest_resolution()
            path_to_download = (r'C:\Users\coloque_seu_diretorio_aqui')
            video.download(path_to_download)
            put_text('Download finalizado!'.title())
            # lembre-se de separar com duas barras nessa parte
            startfile(r'C:\\Users\\coloque_seu_diretorio_aqui')


if __name__ == '__main__':
    video_download()
