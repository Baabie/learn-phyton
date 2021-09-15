print("Bem vindo ao jogo da Adivinhação")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1 

for rodada in range(1, total_de_tentativas + 1):
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
        print("Você acertou")
        break
    #break encerra o ciclo
    elif(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

  #com o for não precisa colocar rodada = rodada + 1  for já faz isso
    print("Fim de jogo")
#iteração repetição de um conjunto de instruções por quantidade finita de vezes ou enquanto uma condição seja aceita