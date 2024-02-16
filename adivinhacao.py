# Dificuldade do jogo
total_de_tentativas = 8
numero_secreto = 1
numero_minimo = 1
numero_maximo = 100

# Torna o número secreto diferente a cada rodada
import random
numero_secreto = random.randint(numero_minimo, numero_maximo)

# Mensagem de Boas Vindas
print("*Bem vindo ao jogo de Adivinhação :) Você terá {:02d} chances para advinhar o número secreto*".format(total_de_tentativas))

# Condição para jogo
for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {:02d} de {:02d}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre {:02d} e {:02d}: ".format(numero_minimo, numero_maximo)))
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