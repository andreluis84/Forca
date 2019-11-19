#importando pacotes e módulos necessários
from random import randint
from utilidades import menu
from utilidades import desenho
from utilidades import palavra
import os

#Chamando o menu principal e o menu de dificuldade
dif=2
opcaoMenu = menu.menu()
if opcaoMenu == 2:
    opcaoDif = menu.dificuldade()
    if opcaoDif == 1:
        dif = 1
        menu.menu()
    elif opcaoDif == 2:
        dif = 2
        menu.menu()
    elif opcaoDif == 3:
        dif = 3
        menu.menu()

print('#' * 17)
print('# JOGO DA FORCA #')
print('#' * 17)
print('')
nome = input('Digite seu nome: ') #Entrada com o nome do jogador

vitoria = 0
derrota = 0
partida = 0

#iniciando o jogo
while True:
    erros = 0
    partida+=1

    #escolhendo a palavra aleatóriamente de acordo com a dificuldade escolhida
    if dif == 1:
        word = palavra.palavraFacil[randint(0, 17)]
        dica = palavra.dicaFacil[palavra.palavraFacil.index(word)]
    elif dif == 2:
        word = palavra.palavraMedio[randint(0, 9)]
        dica = palavra.dicaMedio[palavra.palavraMedio.index(word)]
    elif dif == 3:
        word = palavra.palavraDificil[randint(0, 18)]
        dica = palavra.dicaDificil[palavra.palavraDificil.index(word)]

    temp = []
    letraErr = []

    for letra in word:
        temp.append('_')

    while True:
        # print('\n'*20) # limpa a tela
        os.system('cls')
        desenho.forca(erros)  # imprime desenho da forca

        # imprime a adivinhacao
        print('\n\nAdivinhe: ', end='')

        for let in temp:
            print(let, end=' ')
        print('\n\nLETRAS ERRADAS ',letraErr)
        print('\nDICA:',dica)
        print('\n')

        # Verifica se perdeu
        if erros == 6:
            print('\nLAMENTO, VOCÊ PERDEU!')
            print('A palavra era:',word)
            derrota += 1
            break  # sai do jogo (sai do while)
        # Verificar se o jogador ganhou
        ganhouJogo = True

        for let in temp:
            if let == '_':
                ganhouJogo = False
        if ganhouJogo:
            print('\nPARABÉNS VENCEDOR!!!')
            vitoria += 1
            break
        # captura a letra do usuario
        letraDig = input('{}, informe uma letra: '.format(nome))

        # verifica se acertou alguma letra
        errouLetra = True

        for i, let in enumerate(word):
            if word[i] == letraDig:
                temp[i] = word[i]
                errouLetra = False
        if errouLetra:
            erros = erros + 1
            letraErr.append(letraDig)

    #imprimindo a quantidade de vitórias, derrotas e partidas
    print('\n\nVITÓRIAS: ',vitoria)
    print(f'DERROTAS: ',derrota)
    print(f'PARTIDAS: ',partida)
    print('')

    #dando a opção de jogar novamente
    reload=menu.reload()
    if reload == 1:
        continue
    else:
        break
os.system('cls')
print('OBRIGADO POR JOGAR!')
os.system('pause')
