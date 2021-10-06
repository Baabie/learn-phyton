import forca
import Adivinhação


def escolha_jogo():
    print('************************************************')
    print('********** Bem vindo ao jogo da Forca **********')
    print('************************************************')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual o jogo?'))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando Adivinhação')
        Adivinhação.jogar()
if(__name__ == '__main__'):
    escolha_jogo()