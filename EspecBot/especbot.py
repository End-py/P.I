import os
from tkinter import ttk
import speech_recognition as sr
import numpy as np
import librosa
import sqlite3

os.system('cls')


alt = input('Voce quer ?'
        '\n 1 = ler um arquivo.'
        '\n 2 = gerar um audio.'
        '\n ?: ')


#
local = 'EspecBot/database/audios/'
database = 'EspecBot/database/DataBase.db'
# --

mic = sr.Recognizer()

#
if alt == '2':
    try:
        name = input('Nome:? ')
        file = local + name

        with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source)
            print('Ouvindo...')
            audio = mic.listen(source)

        Text = mic.recognize_google(audio,language='pt-br') # Traduzindo o audio para texto
        #print(Text)

        with open(file + '.wav', 'wb') as save: # Salvando o arquivo de audio
            save.write(audio.get_wav_data())
            print('Audio Salvado.')

    except sr.UnknownValueError:
        print('Não entendi')
        exit()
# --


#
elif alt == '1':
    try:
        name = input('Nome do arquivo?: ')
        file = local + name

        with sr.AudioFile(file + '.wav') as source:
            audio = mic.record(source)

        Text = mic.recognize_google(audio,language='pt-br') # Traduzindo o audio para texto
        #print(Text)

    except sr.UnknownValueError:
        print('Não entendi')
        exit()

    except FileNotFoundError:
        os.system('cls')
        print('Arquivo nao encontrado.')
        exit()

else:
    os.system('cls')
    print('ERRO.')
    exit()
# --


# Audio
data, fs = librosa.load(file +'.wav', sr=44100)
# --


# Dado em espectrograma do audio
dado = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
#print(dado)
# --


# Conectando ao banco de dados
conn = sqlite3.connect(database)
cursor = conn.cursor()
# --


#
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Especdados'")
tabela = cursor.fetchmany()
#print(tabela)

if tabela == [('Especdados',)]:
    print('tabela ja existe')
else:
    print('Criando Tabela')
    cursor.execute("CREATE TABLE Especdados (Code TEXT PRIMARY KEY, Text TEXT, Dado TEXT)")
# --


cursor.execute("SELECT Code FROM Especdados")
coluna = cursor.fetchall()

for li in coluna:
    for num in li:
        #print(num)
        if name in num:
            print('Update Tabela')
            cursor.execute(f"UPDATE Especdados SET Dado = ('{dado}'), Text = ('{Text}') WHERE Code = ('{name}')")
            conn.commit()

        else:
            print('Salvando no Banco de dados')
            cursor.execute(f"INSERT INTO Especdados VALUES('{name}', '{Text}', '{dado}')")
            conn.commit()
# --
