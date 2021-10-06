import random

def jogar():
 #todo o código identado faz parte da função 
    print('******************************************************')
    print('********** Bem vindo ao jogo da Adivinhação **********')
    print('******************************************************')


    numero_secreto = random.randrange(1, 101)  #0.0 1.0
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Define o nível: '))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        #range() permite criar uma sequência de números que variam de um ponte de partida até um ponto final
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    
        chute_str = input("Digite um número entre 1 e 100: ")
    
        print("Você digitou " , chute_str) 
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue 
            #continue para continuar com a próxima iteralção
        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto



        if(acertou): 
            print("Você acertou e fez {} pontos".format(pontos))
            break
        #break encerra o ciclo
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        if(maior):
            print('O seu chute foi maior que o número secreto')
        if(rodada == total_de_tentativas):
            print('O número secreto era {}.Você fez {}'.format(numero_secreto, pontos))
        elif(menor):
            print('Você errou! O seu chute foi menor do que o número secreto.')        
        

        #elif(maior):
            #print("Você errou! O seu chute foi maior do que o número secreto.")
        #elif(menor):
            #print("Você errou! O seu chute foi menor do que o número secreto.")
        
        #pontos_perdidos = abs(numero_secreto - chute)  #40 - 20 = 20  pontos perdidos
        #pontos = pontos - pontos_perdidos   #subtraindo os pontos perdidos da pontuação total

    #com o for não precisa colocar rodada = rodada + 1  for já faz isso
    print("Fim de jogo")
    #iteração repetição de um conjunto de instruções por quantidade finita de vezes ou enquanto uma condição seja aceita
if(__name__ == '__main__'):
    jogar()
