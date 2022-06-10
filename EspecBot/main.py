import os
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import glob
import compare as c
from tqdm import tqdm

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
audio, fs = librosa.load(file +'.wav', sr=44100)
# --


# Plot espectrograma
plt.figure(figsize=(15,6))
audio = librosa.stft(audio, n_fft=2048, hop_length=512, win_length=1024)
audio = np.abs(audio)
librosa.display.specshow(librosa.amplitude_to_db (audio, ref=np.max), x_axis='time', y_axis='log', sr=fs,)
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.savefig(f'EspecBot/database/img/{name}.jpg')
#plt.show()


# Comparando
def trataParametros():
    # Imagem a ser comparada
    img = (f'EspecBot/database/img/{name}.jpg')
    return img

if __name__ == "__main__":
    img = trataParametros()
    images_file_list = glob.glob("EspecBot\database\img\*.jpg") # Diretorio das imagens

    d = {}
    i = 0
    for f in tqdm(images_file_list):
        #print(f)
        score, _, _, _ = c.compare(img, f)
        d[score] = f
        i+=1

# pontuação
    print("\n")
    for i in sorted(d, reverse=True):
        print (i, d[i])
        score, i1, i2, diff = c.compare(img, d[i])
        c.plot(i1, i2, diff, score)
# --
