import numpy as np
import scipy.io.wavfile as wav
from soundPlay import soundPlay as sp

escala = 4
tempo = 0.3
def gera_frequencia(nota):
    freq = 0
    notas = {
        "a": 1,
        "b": 2 + 1,
        "c": 3 + 1,
        "d": 4 + 1,
        "e": 5 + 1,
        "f": 6 + 1,
        "g": 7 + 1,
    }
    escala = {
        "1": 1,
        "2": 2,
        "3": 4,
        "4": 8,
        "5": 16,
        "6": 32,
        "7": 64
    }
    if "" in nota:
        freq = 0
    if "#" in nota:
        for i in range(8):
            if str(i) in nota:
                if str(i) == "0":
                    notaF = notas[nota[0:1]]
                    freq = (2 ** (((notaF) - 49) / 12) * 466.2)
                else:
                    notaF = notas[nota[0:1]]
                    mul = int(escala[nota[2:3]])
                    freq = (2 ** (((notaF) - 49) / 12) * 466.2) * 2 * mul
    else:
        for i in range(8):
            if str(i) in nota:
                if str(i) == "0":
                    notaF = notas[nota[0:1]]
                    freq = (2 ** ((notaF - 49) / 12) * 440)
                else:
                    notaF = notas[nota[0:1]]
                    mul = int(escala[nota[1:2]])
                    freq = (2 ** ((notaF - 49) / 12) * 440) * 2 * mul
    return freq

save = False
musicaSave = np.arange(0,100, 0.001)

def gera_nota(musica):
    global musicaSave
    Fs = 8000
    musicaFinal = []
    for i in range(len(musica)):
        freq = gera_frequencia(str(musica[0]))
        tempo = musica[1]
        t = np.arange(0, tempo, (1. / Fs))
        x = np.cos(2 * np.pi * freq * t)
        ##x = 30000 * x
        if save:
            musicaSave = np.hstack((musicaSave, x))
        else:
            musicaFinal = np.hstack((musicaFinal, x))

    return musicaFinal

goOn = True
c = 2
print("## Bem vindo ao gerador de notas, para sair escreva 'f'.")
print("## Para tocar clique numa tecla das seguintes teclas, 'q','w','e','r','t','y' e 'u'")
print("## Tempo de notas default: 0.3s")
print("## usa 'd' para definições")
print("## usa 'n' para reproduzir a música :)")

while goOn:

    print("usa 's' para activates/desactivar a gravação :)")
    print("Opção: -> ")
    x = str(input())
    if x is 'n':
        sp(musicaSave, 11024)
    elif x is 's':
        if not(save):
            save = True
            print("Está a gravar :)")
        else:
            save = False
            print("Acabou a gravação")
    elif x is 'd':
        print("Alterar escala [1 a 7], escala atual: " + str(escala))
        escala = input("Escala -> ")
        print("Escala alterada para: " + str(escala))
        print("Alterar Tempo [0.01 a 1], tempo atual: " + str(tempo))
        tempo = input("Tempo -> ")
        print("Tempo alterado para: " + str(tempo))
    elif x is 'f':
        goOn = False
    elif x is 'q':
        sp(gera_nota(('a'+str(escala), float(tempo))), 11024)
    elif x is 'w':
        sp(gera_nota(('b'+str(escala), float(tempo))), 11024)
    elif x is 'e':
        sp(gera_nota(('c'+str(escala), float(tempo))), 11024)
    elif x is 'r':
        sp(gera_nota(('d'+str(escala), float(tempo))), 11024)
    elif x is 't':
        sp(gera_nota(('e'+str(escala), float(tempo))), 11024)
    elif x is 'y':
        sp(gera_nota(('f'+str(escala), float(tempo))), 11024)
    elif x is 'u':
        sp(gera_nota(('g'+str(escala), float(tempo))), 11024)