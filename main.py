# Bibliotecas necessárias
import sys
import os
from time import sleep
import webbrowser as wb
from title import ben_title
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
import calendar
import speech_recognition as sr
import pyaudio
import pygame
from pytube import YouTube, Playlist
import wikipedia
from pywinauto import Application, keyboard
import pyautogui


# Funções
def audio_play():
    pygame.mixer.init()
    pygame.mixer.music.load('nome do áudio')
    pygame.mixer.music.play()
    input()


def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print('ouvindo')
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def TextAnimation():
    for i in list(frase):
        print(i, end='')
        sys.stdout.flush()
        sleep(0.03)


def OpenLink():
    link = input('>>>').strip().lower()
    if link == 'youtube':
        wb.open('https://www.youtube.com')


def download_video(video_url):
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download()
    download_video(VIDEO_URL)


def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    for url in playlist:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path='playlist')


def download_audio(video_url):
    yt = YouTube(video_url)
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()
    download_audio(VIDEO_URL)


# Nome do assistente
ben_title()

while True:
    input('\n\033[1;33mPressione ENTER para iniciar\033[m')

    # Solicitação do comando
    frase = '\033[1;36mZoe: Olá, Gustavo! Do que precisa?\n'
    TextAnimation()

    # Abrir microfone
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print('Zoe está ouvindo:')
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        option = texto

    print('')

    # Comandos

    if 'download' in option:
        frase = '''Zoe: O que quer fazer?
    (1) Baixar o vídeo completo
    (2) Baixar apenas o áudio
    (3) Baixar uma playlist\n'''

        TextAnimation()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            choice = texto

        if 'completo' in choice:
            VIDEO_URL = str(input('Link: ')).strip()
            download_video(VIDEO_URL)

        elif 'áudio' in choice:
            VIDEO_URL = str(input('Link: ')).strip()
            download_audio(VIDEO_URL)

        elif 'playlist' in choice:
            VIDEO_URL = str(input('Link: ')).strip()
            download_playlist(VIDEO_URL)


    elif 'playlist' in option:
        frase = 'Zoe: Qual Playlist deseja acessar?\n'
        TextAnimation()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            choice = texto

        if "estudo" in choice:
            frase = 'Zoe: Abrindo sua playlist de Estudo...'
            TextAnimation()
            sleep(1.5)
            wb.open('https://www.youtube.com/playlist?list=PLTtf8SgF7Uvctu3yCbsiIe1eURKbatWab')

        elif "Games" in choice:
            frase = 'Zoe: Abrindo sua playlist de Gaming...'
            TextAnimation()
            sleep(1.5)
            wb.open('https://www.youtube.com/playlist?list=PLTtf8SgF7Uves8CBRi3ZoO3Leyp2bjkWG')

    if 'YouTube' in option:
        frase = 'Zoe: Abrindo YouTube...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.youtube.com')

    elif 'Twitter' in option:
        frase = 'Zoe: Abrindo Twitter...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://twitter.com/home')

    elif 'dizer' in option:
        frase = 'Zoe: Abrindo Deezer...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.deezer.com/br/')

    elif 'faculdade' in option:
        frase = 'Zoe: Abrindo portal do aluno...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://estudantesuam.ead.br')

    elif 'Netflix' in option:
        frase = 'Zoe: Acessando Netflix...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.netflix.com/browse')

    elif 'calculadora' in option:
        from calculadora import *

        calculator()

    elif 'notas' in option:
        from notepad import notepad

        notepad()

    elif 'comandos' in option:
        frase = 'Zoe: Acessando lista de comandos...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://docs.google.com/document/d/1MCkMocfxs8lZUjG-bXtOGufNCgOkaIUW_7ZXEvpYc08/edit?usp=sharing')

    elif 'valorant' in option:
        frase = 'Zoe: Buscando vídeos de Valorant...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.youtube.com/results?search_query=valorant')

    elif 'Amazon' in option:
        frase = 'Zoe: Abrindo Amazon...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.amazon.com.br')

    elif 'Prime' in option:
        frase = 'Zoe: Abrindo Prime Vídeo...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.primevideo.com')

    elif 'Disney' in option:
        frase = 'Zoe: Abrindo Disney Plus...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.disneyplus.com/pt-br/login')

    elif 'Google' in option:
        frase = 'Zoe: O que deseja pesquisar?\n'
        TextAnimation()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            choice = texto

        print(f'Zoe: OK! Buscando {choice} no Google...')
        sleep(1)
        navegador = webdriver.Chrome()
        navegador.get('https://www.google.com')
        sleep(1)
        navegador.find_element(By.XPATH,
                               '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
            choice)
        navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

    elif 'ajuda' in option:
        frase = 'Zoe: Acessando informações...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://docs.google.com/document/d/14VFEKeG2JmXEYgBmO__yXcQKeB9IU2Eioe8etTv7wd0/edit?usp=sharing')

    elif 'trabalho' in option:
        frase = 'Zoe: Executando trabalho...\n'
        TextAnimation()
        navegador = webdriver.Chrome()
        navegador.get('https://sgf.fisk.com.br:154/SGF/Auth/Login?ReturnUrl=%2Fsgf%2F')
        sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="Login"]').send_keys('Gchotti')
        navegador.find_element(By.XPATH, '//*[@id="Password"]').send_keys('Nickmane16')
        navegador.find_element(By.XPATH, '/html/body/div[2]/div/a[2]').click()
        navegador.find_element(By.XPATH, '//*[@id="submitLogin"]').click()

    elif 'programar' in option:
        frase = 'Zoe: Hora de programar então...\n'
        TextAnimation()
        sleep(1.5)
        wb.open('https://replit.com/~')

    elif 'data' in option:
        data_atual = date.today()
        weekday = calendar.day_name[data_atual.weekday()]
        if 'Monday' in weekday:
            print(f'Zoe: Hoje é Segunda-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
        elif 'Tuesday' in weekday:
            print(f'Zoe: Hoje é Terça-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
        elif 'Wednesday' in weekday:
            print(f'Zoe: Hoje é Quarta-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
        elif 'Thursday' in weekday:
            print(f'Zoe: Hoje é Quinta-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
        elif ' Friday' in weekday:
            print(f'Zoe: Hoje é Sexta-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
        elif 'Saturday' in weekday:
            print(f'Zoe: Hoje é Sábado. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
        elif 'Sunday' in weekday:
            print(f'Zoe: Hoje é Domingo. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')

    elif 'sair' in option:
        print('Zoe: Tchau!')
        sys.exit()

    elif 'canva' in option:
        frase = 'Zoe: Abrindo Canva...\n'
        TextAnimation()
        sleep(1.5)
        wb.open('https://www.canva.com')

    elif 'senhas' in option:
        frase = 'Zoe: Executando gerador de senhas...\n'
        TextAnimation()
        sleep(1.5)
        import password_generator

        exec(password_generator)

    elif 'joquempô' in option:
        frase = 'Zoe: Abrindo Jokenpo...\n'
        TextAnimation()
        import jokenpo

        exec(jokenpo)

    elif 'velha' in option:
        frase = 'Zoe: Abrindo Jogo da Velha...\n'
        TextAnimation()
        import jogo_da_velha

        exec(jogo_da_velha)

    elif 'forca' in option:
        frase = 'Zoe: Abrindo Jogo da Forca...\n'
        TextAnimation()
        import jogo_da_forca

        exec(jogo_da_forca)

    elif 'drive' in option:
        frase = 'Zoe: Abrindo Google Drive...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://drive.google.com/drive/my-drive')

    elif 'desligar' in option:
        frase = 'Gostaria de desligar seu computador ? (sim / não)'
        TextAnimation()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            choice = texto

        if choice == 'não':
            exit()
        elif choice == 'sim':
            os.system("shutdown /s /t 1")
        else:
            frase = 'Resposta inválida!'
            TextAnimation()

    elif 'traduzir' in option:
        frase = 'Zoe: Abrindo Google Tradutor...'
        TextAnimation()
        sleep(1.5)
        wb.open('https://translate.google.com.br/?hl=pt-BR')

    elif 'Wikipédia' in option:

        frase = 'Zoe: O que deseja pesquisar no Wikipédia?\n'
        TextAnimation()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            keyword = texto

            print('')

            wikipedia.set_lang("pt")
            pesquisa1 = wikipedia.summary(keyword)[0:150]
            pesquisa2 = wikipedia.summary(keyword)[150:300]
            pesquisa3 = wikipedia.summary(keyword)[300:450]
            pesquisa4 = wikipedia.summary(keyword)[450:600]
            print(pesquisa1)
            print(pesquisa2)
            print(pesquisa3)
            print(pesquisa4)

            print('')

            frase = 'Deseja salvar este conteúdo? '
            TextAnimation()

            print('')

            rec = sr.Recognizer()
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                print('Zoe está ouvindo:')
                audio = rec.listen(mic)
                texto = rec.recognize_google(audio, language='pt-BR')
                choice = texto

            if 'sim' in choice:
                app = Application().start('notepad.exe')
                pesquisa = wikipedia.summary(keyword)[0:600]
                app.UntlitedNotepad.Edit.type_keys(pesquisa, with_spaces=True)
                pyautogui.hotkey('ctrl', 's')
                sleep(0.5)
                pyautogui.write(keyword)
                sleep(0.5)
                pyautogui.hotkey('enter')

            else:
                pass


    elif 'escrita' in option:
        frase = 'Zoe: Diga o que deseja que eu escreva para você...\n'
        TextAnimation()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            content = rec.recognize_google(audio, language='pt-BR')

        app = Application().start('notepad.exe')

        app.UntlitedNotepad.Edit.type_keys(content, with_spaces=True)
        keyboard.send_keys('{ENTER}')
        sleep(1)

        pyautogui.hotkey('ctrl', 's')
        sleep(0.5)
        pyautogui.write('text')
        sleep(0.5)
        pyautogui.hotkey('enter')
