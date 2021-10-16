import os
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

os.system('cls')

alt = input('Voce quer ?'
        '\n 1 = ler um arquivo.'
        '\n 2 = gerar um audio.'
        '\n ?: ')

local = 'EspecBot/audios/'
database = 'EspecBot/database/'

if alt == '2':
    try:
        name = input('Nome:? ')
        file = local + name

        mic = sr.Recognizer()

        with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source)
            print('Ouvindo...')
            audio = mic.listen(source)

        Text = mic.recognize_google(audio,language='pt-br')
        #print(Text)

        with open(file + '.wav', 'wb') as save:
            save.write(audio.get_wav_data())
            print('Audio Salvado.')

    except sr.UnknownValueError:
        print('Não entendi')
        exit()

elif alt == '1':
    try:
        name = input('Nome do arquivo?: ')
        file = local + name

        data, fs = librosa.load(file +'.wav', sr=44100)

    except FileNotFoundError:
        os.system('cls')
        print('Arquivo nao encontrado.')
        exit()

else:
    os.system('cls')
    print('ERRO.')
    exit()


# #
# savefig = database + name

# plt.figure(figsize=(12, 6))

# fig1 = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
# librosa.display.specshow(fig1, x_axis='time', y_axis='linear', sr=fs, cmap='jet')

# plt.title('Espectrograma')
# plt.xlabel('Time [s]')
# plt.ylabel('Frequecy [Hz]')
# plt.colorbar(format='%+2.0f dB')
# plt.savefig(savefig + '_fig1.jpg')
# print('Figura 1 Salvada.  :)')
# plt.show()
# # --


# #
# plt.figure(figsize=(12, 6))

# fig2 = np.arange(0, len(data)* 1/fs, 1/fs)

# plt.plot(fig2, data)
# plt.xlabel('Time [s]')
# plt.ylabel('Frequecy [Hz]')
# plt.savefig(savefig + '_fig2.jpg')
# print(CYAN + 'Figura 2 Salvada.  :)')
# plt.show()
# # --


dado = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
print(dado)