# Bibliotecas:
from pytube import YouTube, Playlist

# URL do vídeo ou playlist:
VIDEO_URL = 'https://www.youtube.com/watch?v=6_xVsr4-4rU'
PLAYLIST_URL = 'colar aqui a URL da playlist'


# Download de vídeos:
def download_video(video_url):
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download()
    download_video(VIDEO_URL)


# Download de Playlist:
def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    for url in playlist:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path='playlist')
        download_playlist(PLAYLIST_URL)


# Download de Áudio:
def download_audio(video_url):
    yt = YouTube(video_url)
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()
    download_audio(VIDEO_URL)