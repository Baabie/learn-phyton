print("Bem vindo ao jogo da Adivinhação")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Você digitou " , chute_str) 

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou): 
    print("Você acertou")
elif(maior):
    print("Você errou! O seu chute foi maior do que o número secreto.")
elif(menor):
    print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim de jogo")
