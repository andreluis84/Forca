import os

#menu principal
def menu():
    print('#' * 17)
    print('# JOGO DA FORCA #')
    print('#' * 17)
    print('')
    print('1 - Jogar')
    print('2 - Dificuldade')
    print('')
    opcao = int(input('Digite a sua opção: '))
    os.system('cls')
    return opcao

#menu de dificuldades
def dificuldade():
    print('#' * 17)
    print('# JOGO DA FORCA #')
    print('#' * 17)
    print('')
    print('DIFICULDADE')
    print('1 - Fácil')
    print('2 - Médio')
    print('3 - Difícil')
    print('')
    opcao = int(input('Digite a sua opção: '))
    os.system('cls')
    return opcao

#menu do continue
def reload():
    print('1 - Continuar')
    print('2 - Sair')
    opcao = int(input('Digite a sua opção: '))
    #os.system('cls')
    return opcao