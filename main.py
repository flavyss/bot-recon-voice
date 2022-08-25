from cgitb import text
from tkinter import *
import json
import datetime
from turtle import color
import speech_recognition as sr
import sounddevice as sd
import wavio as wv
import wikipedia
import webbrowser
import random
from gtts import gTTS
import pyautogui
from playsound import playsound
import pywhatkit as kit
import bs4
import joblib
import os
import requests

def speak(text):
    global filevoice
    for a in range(0,3):
        gtts = gTTS(text, lang='pt')
        filevoice = str('audio00' + str(a) + '.mp3')
        gtts.save('audio/'+filevoice)
    playsound('audio/'+filevoice, True)
    os.remove('audio/'+filevoice)

def actionIA():

    filename = "myvoice.wav"
    
    def listen():
        freq = 48000  # Altere a frequência se achar necessário
        duration = 5  # Altere a duração de cada gravação
        recording = sd.rec(int(duration * freq),
        samplerate=freq, channels=2)
        print('estou ouvindo')
        sd.wait()
        wv.write("myvoice.wav", recording, freq, sampwidth=2)
        print('Processando...')

    speak("estou ouvindo")

    while True:
        listen()

        #possiveis falas:

        r = sr.Recognizer()

        try:
            with sr.AudioFile(filename) as source:

                audio_data = r.record(source)
                says = r.recognize_google(audio_data, language='pt-BR')

                print('Você: ' + says.lower())
                texto = says.lower()

            saudacoes = open("data/fulltext/saudacoes.txt", 'r')
            saudacao = saudacoes.read()
            encerramentos = open("data/fulltext/close.txt", 'r')
            encerrar = encerramentos.read()

            if texto in saudacao :
                speak('salve salve')

            elif texto in encerrar:
                speak("tchau tchau, foi um prazer trabalhar com você")
                janela.destroy()
                break

            elif 'toque' in texto or 'tocar' in texto:
                search = texto.replace('toque', '')
                speak("sim senhor! Tocando música")
                kit.playonyt(search)

            elif 'abrir' in texto:
                search = texto.replace('abrir', '')
                speak("sim senhor! Abrindo site que pediu")
                url = f'{search}.com'
                webbrowser.open(url)

            elif 'envie uma mensagem' in texto:

                hora = datetime.datetime.now().strftime('%H')
                minut = datetime.datetime.now().strftime('%M')
                minuto = int(minut) + 1

                db = {
                    'flávio':'+558185296020',
                    'mateus':'+558183120438'
                }   
                speak('qual o nome do receptor? ')
                listen()

                with sr.AudioFile(filename) as source:

                    audio_data = r.record(source)
                    says = r.recognize_google(audio_data, language='pt-BR')

                    print('Você: ' + says.lower())
                    search = says.lower()
                if search in db:
                    speak('qual a mensagem? ')
                    listen()

                    with sr.AudioFile(filename) as source:

                        audio_data = r.record(source)
                        says = r.recognize_google(audio_data, language='pt-BR')
                        print('Você: ' + says.lower())
                        message = says.lower()

                    kit.sendwhatmsg(db[search], message, int(hora),int(minuto))
                    pyautogui.press('enter')
                    speak('Menssagem Enviada com Sucesso')

                


        except Exception as e:
            print('Ocorreu algum erro, fale novamente')

janela = Tk()
janela.title('Assistente Virtual em Python - Dev')
janela.configure(bg='black')
janela.geometry('890x500+0+0')

label_l = Label(janela, text='E.L.F.A', font='Arial 60', background='black', foreground='aqua')
label_l.pack(side='top')

botao_l = Button(janela, height=2, width=100, text='Iniciar',font=30,foreground='aqua', command=actionIA, background='#333')
botao_l.pack(side='bottom')


janela.mainloop()
