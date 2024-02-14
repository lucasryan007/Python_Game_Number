#Mensagem de Boas Vindas
print(" Bem vindo ao jogo de Adivinhação :) Você terá 3 chances para advinhar o número de 1 até 50 *")

#Tentativas até o Game Over
total_de_tentativas = 3

#Condição para jogo
while(total_de_tentativas > 0):
    print("Quantidade de Chances", total_de_tentativas)

#Variáveis
    numero_secreto = 42
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)
    acertou_numero = numero_secreto == chute
    errou_numero = numero_secreto < chute

#Funções
    if (acertou_numero):
        total_de_tentativas -=3
    elif (errou_numero):
        print("Você errouuu! O seu chute foi maior do que o número secreto")
        total_de_tentativas -= 1
    else:
        print("Você errouuu! O seu chute foi menor do que o número secreto")
        total_de_tentativas -= 1

#Mensagem final do jogo
if (acertou_numero) == True:
    print("Você acertou :) Fim de Jogo")
elif total_de_tentativas == 0:
    print("Fim de jogo, você não descobriu o número :(")