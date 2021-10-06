
import os

import speech_recognition as sr
from gtts import gTTS
from IPython.display import Audio

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display


# color
BLACK  = '\033[1;30m'
BLUE   = '\033[1;34m'
GREEN  = '\033[1;32m'
CYAN   = '\033[1;36m'
RED    = '\033[1;31m'
PURPLE = '\033[1;35m'
BROWN  = '\033[1;33m'
GRAY   = '\033[1;37m'
YELLOW = '\033[1;33m'
WHITE  = '\033[1;37m'
# --


os.system('cls')


#
local_a = 'BotEspec/audios/'
local_i = 'BotEspec/img/'

alt = input(CYAN + 'Voce quer ?' +
        YELLOW + '\n 1 =' + CYAN + ' ler um arquivo.' +
        YELLOW + '\n 2 =' + CYAN + ' gerar um audio.' +
        BLUE + '\n ?: ')
# --


#
if alt == '1':
    try:
        nome = input(CYAN + 'Nome do arquivo?: ')
        arquivo = local_a + nome
        data, fs = librosa.load(arquivo +'.wav', sr=44100)

    except FileNotFoundError:
        os.system('cls')
        print(RED + 'ERRO' + CYAN + ' Arquivo nao encontrado.')
        exit()

elif alt == '2':

    nome = input(CYAN + 'Nome do arquivo?: ')
    arquivo = local_a + nome

    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print(CYAN + 'Ouvindo... ')
        audio = microfone.listen(source)

    with open(arquivo + '.wav', 'wb') as save:
        save.write(audio.get_wav_data())
        print('Audio Salvado.  :)')

    data, fs = librosa.load(arquivo + '.wav', sr=44100)

else:
    print(RED + 'ERRO.  :(')
    exit()
# --


savefig = local_i + nome


#
plt.figure(figsize=(12, 6))

fig1 = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
librosa.display.specshow(fig1, x_axis='time', y_axis='linear', sr=fs, cmap='jet')

plt.title('Espectrograma')
plt.xlabel('Time [s]')
plt.ylabel('Frequecy [Hz]')
plt.colorbar(format='%+2.0f dB')
plt.savefig(savefig + '_fig1.jpg')
print(CYAN + 'Figura 1 Salvada.  :)')
plt.show()
# --


#
plt.figure(figsize=(12, 6))

fig2 = np.arange(0, len(data)* 1/fs, 1/fs)

plt.plot(fig2, data)
plt.xlabel('Time [s]')
plt.ylabel('Frequecy [Hz]')
plt.savefig(savefig + '_fig2.jpg')
print(CYAN + 'Figura 2 Salvada.  :)')
plt.show()
# --
