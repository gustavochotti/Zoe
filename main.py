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
import pyttsx3


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


def voice():
    engine = pyttsx3.init()
    engine.say(frase)
    engine.runAndWait()


# Nome do assistente
ben_title()

engine = pyttsx3.init()
engine.say('Olá, eu sou a Zoi! Sua Assistente virtual!')
engine.runAndWait()

while True:
    input('Pressione ENTER para iniciar')

    # Solicitação do comando
    engine = pyttsx3.init()
    engine.say('Do que precisa?')
    engine.runAndWait()

    # Abrir microfone
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print('Zoe está ouvindo')
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        option = texto

    print('')

    # Comandos

    if 'download' in option:

        frase = '''O que quer fazer?
    (1) Baixar o vídeo completo
    (2) Baixar apenas o áudio
    (3) Baixar uma playlist\n'''
        voice()

        sleep(0.7)
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            choice = texto

        if 'completo' in choice:
            frase = 'cole o link'
            voice()
            VIDEO_URL = str(input('Link: ')).strip()
            download_video(VIDEO_URL)


        elif 'áudio' in choice:
            frase = 'cole o link'
            voice()
            VIDEO_URL = str(input('Link: ')).strip()
            download_audio(VIDEO_URL)

        elif 'playlist' in choice:
            frase = 'cole o link'
            voice()
            VIDEO_URL = str(input('Link: ')).strip()
            download_playlist(VIDEO_URL)



    elif 'playlist' in option:
        engine = pyttsx3.init()
        engine.say('Qual Playlist deseja acessar?')
        engine.runAndWait()

        sleep(0.7)
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            choice = texto
            sleep(0.7)

        if "estudo" in choice:
            engine = pyttsx3.init()
            engine.say('Abrindo sua playlist de Estudo...')
            engine.runAndWait()
            wb.open('https://www.youtube.com/playlist?list=PLTtf8SgF7Uvctu3yCbsiIe1eURKbatWab')

        elif "Games" in choice:
            engine = pyttsx3.init()
            engine.say('Abrindo sua playlist de Gaming...')
            engine.runAndWait()
            wb.open('https://www.youtube.com/playlist?list=PLTtf8SgF7Uves8CBRi3ZoO3Leyp2bjkWG')

        elif 'braba' in choice:
            engine = pyttsx3.init()
            engine.say('Abrindo playlist só as brabas...')
            engine.runAndWait()
            wb.open('https://www.youtube.com/playlist?list=PLTtf8SgF7UveHi6xZTAKhj8ZbgGYmosWW')


    if 'YouTube' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo YouTube...')
        engine.runAndWait()
        wb.open('https://www.youtube.com')

    elif 'Twitter' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Twitter...')
        engine.runAndWait()

        wb.open('https://twitter.com/home')

    elif 'dizer' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Deezer...')
        engine.runAndWait()
        pyautogui.hotkey('win')
        sleep(0.5)
        pyautogui.write('deezer Music')
        sleep(0.5)
        pyautogui.hotkey('enter')

    elif 'Netflix' in option:
        engine = pyttsx3.init()
        engine.say('Acessando Netflix...')
        engine.runAndWait()
        wb.open('https://www.netflix.com/browse')

    elif 'calculadora' in option:
        engine = pyttsx3.init()
        engine.say('Acessando Calculadora...')
        engine.runAndWait()
        from calculadora import *

        calculator()

    elif 'notas' in option:
        engine = pyttsx3.init()
        engine.say('Acessando Bloco de notas...')
        engine.runAndWait()
        from notepad import notepad

        notepad()

    elif 'comandos' in option:
        engine = pyttsx3.init()
        engine.say('Acessando lista de comandos...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://github.com/gustavochotti/Zoe/blob/main/commands')

    elif 'valorant' in option:
        engine = pyttsx3.init()
        engine.say('Buscando vídeos de Valorant...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://www.youtube.com/results?search_query=valorant')

    elif 'Amazon' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Amazon...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://www.amazon.com.br')

    elif 'Prime' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Prime Vídeo...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://www.primevideo.com')

    elif 'Disney' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Disney Plus...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://www.disneyplus.com/pt-br/login')

    elif 'Google' in option:
        engine = pyttsx3.init()
        engine.say('O que deseja pesquisar?')
        engine.runAndWait()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            choice = texto

        engine = pyttsx3.init()
        engine.say(f'OK! Buscando {choice} no Google...')
        engine.runAndWait()
        sleep(1)
        navegador = webdriver.Chrome()
        navegador.get('https://www.google.com')
        sleep(1)
        navegador.find_element(By.XPATH,
                               '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
            choice)
        navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

    elif 'ajuda' in option:
        engine = pyttsx3.init()
        engine.say('Acessando manual do usuário...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://github.com/gustavochotti/Zoe/blob/main/user_manual')


    elif 'data' in option:
        data_atual = date.today()
        weekday = calendar.day_name[data_atual.weekday()]
        if 'Monday' in weekday:
            engine = pyttsx3.init()
            engine.say(f'Hoje é Segunda-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
            engine.runAndWait()
        elif 'Tuesday' in weekday:
            engine = pyttsx3.init()
            engine.say(f'Hoje é Terça-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
            engine.runAndWait()
        elif 'Wednesday' in weekday:
            engine = pyttsx3.init()
            engine.say(f'Hoje é Quarta-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
            engine.runAndWait()
        elif 'Thursday' in weekday:
            engine = pyttsx3.init()
            engine.say(f'Hoje é Quinta-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
            engine.runAndWait()
        elif ' Friday' in weekday:
            engine = pyttsx3.init()
            engine.say(f'Hoje é Sexta-Feira. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
            engine.runAndWait()
        elif 'Saturday' in weekday:
            engine = pyttsx3.init()
            engine.say(f'Hoje é Sábado. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
            engine.runAndWait()
        elif 'Sunday' in weekday:
            engine = pyttsx3.init()
            engine.say(f'Hoje é Domingo. Dia {data_atual.day} do {data_atual.month} de {data_atual.year}. ')
            engine.runAndWait()

    elif 'sair' in option:
        engine = pyttsx3.init()
        engine.say('Tchau!')
        engine.runAndWait()
        sys.exit()


    elif 'senhas' in option:
        engine = pyttsx3.init()
        engine.say('Executando gerador de senhas...')
        engine.runAndWait()
        sleep(1.5)
        import password_generator

        exec(password_generator)

    elif 'joquempô' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Jokenpo...')
        engine.runAndWait()
        import jokenpo

        exec(jokenpo)

    elif 'velha' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Jogo da Velha...')
        engine.runAndWait()
        import jogo_da_velha

        exec(jogo_da_velha)

    elif 'forca' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Jogo da Forca...')
        engine.runAndWait()
        import jogo_da_forca

        exec(jogo_da_forca)

    elif 'desligar' in option:
        frase = 'Gostaria de desligar seu computador ? (sim / não)'

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

    elif 'tradutor' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Google Tradutor...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://translate.google.com.br/?hl=pt-BR')

    elif 'Wikipédia' in option:

        # frase = 'O que deseja pesquisar no Wikipédia?\n'
        engine = pyttsx3.init()
        engine.say('O que deseja pesquisar no Wikipédia?')
        engine.runAndWait()

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
            sleep(5)
            choice = input('Deseja salvar este conteúdo? ')

            print('')

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

    elif 'escreva' in option:
        # frase = 'Diga o que deseja que eu escreva para você...\n'
        engine = pyttsx3.init()
        engine.say('Diga o que deseja que eu escreva para você...')
        engine.runAndWait()

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

    elif 'web' in option:
        engine = pyttsx3.init()
        engine.say('Executando procedimento para instalação do webdriver...')
        engine.runAndWait()

        engine = pyttsx3.init()
        engine.say('Você já possui o Python instalado em sua máquina?')
        engine.runAndWait()

        choice = str(input('S/N: ')).strip().lower()

        if 'n' in choice:
            engine = pyttsx3.init()
            engine.say('Certo, antes de continuarmos então, vou precisar que você faça a instalação dele.')
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say('Abrindo site para download do Python...')
            engine.runAndWait()
            wb.open('https://www.python.org/downloads/')
            engine = pyttsx3.init()
            engine.say('Assim que finalizar a instalação, pressione enter abaixo, para continuar o processo...')
            engine.runAndWait()
            input('Pressione ENTER para continuar')
            pass

        elif 's' in choice:
            pass

        engine = pyttsx3.init()
        engine.say('Seu sistema operacional é windows, mac ou linux')
        engine.runAndWait()

        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Zoe está ouvindo:')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language='pt-BR')
            sistem = texto

        if 'Windows' in sistem:
            engine = pyttsx3.init()
            engine.say('Qual a versão do seu Google Chrome? 101, 102 ou 103?')
            engine.runAndWait()

            rec = sr.Recognizer()
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                print('Zoe está ouvindo:')
                audio = rec.listen(mic)
                texto = rec.recognize_google(audio, language='pt-BR')
                choice = texto

                engine = pyttsx3.init()
                engine.say('Ok, para continuar vou te redirecionar para o link de download do driver de seu navegador')
                engine.runAndWait()

                engine = pyttsx3.init()
                engine.say('Assim que concluir o download, pressione enter para continuarmos')
                engine.runAndWait()

            if '101' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.101')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1kNx7CPsppKENhcSNAsC7QHZxE_LCuPfq&export=download')
                input('Pressione ENTER para continuar')
                pass

            elif '102' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.102')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1u4GsF35RXD-XFHc9U-PpmwxLVbiE2rmc&export=download')
                input('Pressione ENTER para continuar')
                pass

            elif '103' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.103')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1-toEfG8hIMZ4h3D_l1Svmg0ne8akSsjQ&export=download')
                input('Pressione ENTER para continuar')
                pass

        if 'Mac' in sistem:
            engine = pyttsx3.init()
            engine.say('Qual a versão do seu Google Chrome? 101, 102 ou 103?')
            engine.runAndWait()

            rec = sr.Recognizer()
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                print('Zoe está ouvindo:')
                audio = rec.listen(mic)
                texto = rec.recognize_google(audio, language='pt-BR')
                choice = texto

                engine = pyttsx3.init()
                engine.say('Ok, para continuar vou te redirecionar para o link de download do driver de seu navegador')
                engine.runAndWait()

                engine = pyttsx3.init()
                engine.say('Assim que concluir o download, pressione enter para continuarmos')
                engine.runAndWait()

            if '101' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.101')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1tuTInrcEvz2CnMtIFST7iF-dNZD7Te2s&export=download')
                input('Pressione ENTER para continuar')
                pass

            elif '102' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.102')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1NFckemb7pUxvfmAn919tTwjjBWTY-xXI&export=download')
                input('Pressione ENTER para continuar')
                pass

            elif '103' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.103')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=16Lg9JYyUoPi-4oLStu7nwGVip-_cN5dQ&export=download')
                input('Pressione ENTER para continuar')
                pass

        elif 'Linux' in sistem:
            engine = pyttsx3.init()
            engine.say('Qual a versão do seu Google Chrome? 101, 102 ou 103?')
            engine.runAndWait()

            rec = sr.Recognizer()
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                print('Zoe está ouvindo:')
                audio = rec.listen(mic)
                texto = rec.recognize_google(audio, language='pt-BR')
                choice = texto

                engine = pyttsx3.init()
                engine.say('Ok, para continuar vou te redirecionar para o link de download do driver de seu navegador')
                engine.runAndWait()

                engine = pyttsx3.init()
                engine.say('Assim que concluir o download, pressione enter para continuarmos')
                engine.runAndWait()

            if '101' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.101')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1t2-eP_6bszNCWtTIX09-Y_TYj3jNsGRN&export=download')
                input('Pressione ENTER para continuar')
                pass

            elif '102' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.102')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1In35okoPMDvY9Kcp0fPN1VRlaqr8ec-b&export=download')
                input('Pressione ENTER para continuar')
                pass

            elif '103' in choice:
                engine = pyttsx3.init()
                engine.say('Abrindo Link para download do chromedriver.103')
                engine.runAndWait()
                wb.open('https://drive.google.com/u/0/uc?id=1vNxl2ZUrhrUV6EGWCsgYrZ8Zk9RlvqjO&export=download')
                input('Pressione ENTER para continuar')
                pass

        engine = pyttsx3.init()
        engine.say('Agora busque em sua máquina a pasta em que está instalado o seu Python')
        engine.runAndWait()
        engine = pyttsx3.init()
        engine.say('Assim que encontrar, cole o driver que você baixou nesta pasta')
        engine.runAndWait()
        engine = pyttsx3.init()
        engine.say('E pronto, procedimento de Web concluído. Você já pode realizar pesquisas automáticas no Google.')
        engine.runAndWait()

        engine = pyttsx3.init()
        engine.say('Qualquer dúvida em relação a este processo, basta solicitar ajuda nos comandos e seguir as '
                   'instruções presentes no vídeo do aviso 2')
        engine.runAndWait()

    elif 'jogar' in option:
        pyautogui.hotkey('win')
        sleep(0.5)
        pyautogui.write('nitro')
        sleep(0.5)
        pyautogui.hotkey('enter')
        sleep(1)
        pyautogui.hotkey('win')
        sleep(0.5)
        pyautogui.write('Escolher um plano de energia')
        sleep(0.5)
        pyautogui.hotkey('enter')
        sleep(1)
        pyautogui.hotkey('win')
        sleep(0.5)
        pyautogui.write('Throttlestop.exe')
        sleep(1.2)
        pyautogui.hotkey('enter')

    elif 'drive' in option:
        frase = 'Abrindo Google Drive...'
        sleep(1.5)
        wb.open('https://drive.google.com/drive/my-drive')

    elif 'programar' in option:
        engine = pyttsx3.init()
        engine.say('Ok, abrindo programação')
        engine.runAndWait()
        pyautogui.hotkey('win')
        sleep(0.5)
        pyautogui.write('Pycharm')
        sleep(0.5)
        pyautogui.hotkey('enter')

    elif 'canva' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Canva...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://www.canva.com')

    elif 'Twitch' in option:
        engine = pyttsx3.init()
        engine.say('Abrindo Twitch...')
        engine.runAndWait()
        sleep(1.5)
        wb.open('https://www.twitch.tv')
