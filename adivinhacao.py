# Mensagem de Boas Vindas
print("*Bem vindo ao jogo de Adivinhação :) Você terá 3 chances para advinhar o número de 1 até 50*")

# Tentativas até o Game Over e rodadas
total_de_tentativas = 3

# Definição de número secreto
numero_secreto = 42

# Condição para jogo
for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite o seu número: "))
    acertou_numero = numero_secreto == chute
    chute_maior = numero_secreto < chute
    chute_menor = numero_secreto > chute

    # Funções acerto ou erro
    if (acertou_numero):
        print("Você acertou :) Fim de jogo!")
        break
    elif (chute_maior):
        print("Você errou! O seu chute foi maior do que o número secreto!")
    elif (chute_menor):
        print("Você errou! O seu chute foi menor do que o número secreto!")

if not (acertou_numero):
    print("Fim de jogo, você não descobriu o número secreto que era: {}".format(numero_secreto))