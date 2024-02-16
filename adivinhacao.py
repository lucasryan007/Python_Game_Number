# Dificuldade do jogo
total_de_tentativas = 5
numero_secreto = 42
numero_minimo = 1
numero_maximo = 100

# Mensagem de Boas Vindas
print("*Bem vindo ao jogo de Adivinhação :) Você terá {} chances para advinhar o número secreto*".format(total_de_tentativas))

# Condição para jogo
for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre {} e {}: ".format(numero_minimo, numero_maximo)))
    acertou_numero = numero_secreto == chute
    chute_maior = numero_secreto < chute
    chute_menor = numero_secreto > chute

    # Funções acerto ou erro
    if (chute < 1):
        print("Você digitou um número menor do que {}".format(numero_minimo))
        continue
    elif (chute > 100):
        print("Você digitou um número maior do que {}".format(numero_maximo))
        continue
    elif (acertou_numero):
        print("Você acertou :) Fim de jogo!")
        break
    elif (chute_maior):
        print("Você errou! O seu chute foi maior do que o número secreto!")
    elif (chute_menor):
        print("Você errou! O seu chute foi menor do que o número secreto!")

if not (acertou_numero):
    print("Fim de jogo, você não descobriu o número secreto que era: {}".format(numero_secreto))