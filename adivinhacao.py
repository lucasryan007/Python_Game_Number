# Mensagem de Boas Vindas e importações
import random
print("*Bem vindo ao jogo de Adivinhação :)*")
print("Escolha o nível de dificuldade:")
print("(1) Fácil (2) Médio (3) Difícil")


# Variaveis de dificuldade do jogo e pontuação
total_de_tentativas = 8
numero_secreto = 80
numero_minimo = 1
numero_maximo = 100
nivel = 0
pontos = 100

# Jogador escolhe o nível que quer jogar
while (nivel >= 1 or nivel <= 3):
    nivel = int(input("Defina a dificuldade: "))
    if (nivel == 1):
        numero_minimo = 1
        numero_maximo = 50
        total_de_tentativas = 10
        print("Você terá {:02d} tentativas!".format(total_de_tentativas))
        break
    elif (nivel == 2):
        numero_minimo = 1
        numero_maximo = 50
        total_de_tentativas = 5
        print("Você terá {:02d} tentativas!".format(total_de_tentativas))
        break
    elif (nivel == 3):
        numero_minimo = 1
        numero_maximo = 100
        total_de_tentativas = 5
        print("Você terá {:02d} tentativas!".format(total_de_tentativas))
        break
    print("Digite uma dificuldade válida entre 1 e 3")

# Torna o número secreto diferente a cada rodada
numero_secreto = random.randint(numero_minimo, numero_maximo)
print(numero_secreto)

# Condição para jogo
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {:02d} de {:02d}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre {:02d} e {:02d}: ".format(numero_minimo, numero_maximo)))
    acertou_numero = numero_secreto == chute
    chute_maior = numero_secreto < chute
    chute_menor = numero_secreto > chute

    # Caso jogador escolha um numero incorreto
    if (chute < 1):
        print("Você digitou um número menor do que {}".format(numero_minimo))
        pontos -= 20
        continue
    elif (chute > 100):
        print("Você digitou um número maior do que {}".format(numero_maximo))
        pontos -= 20
        continue
    # Funções de acerto ou erro
    elif (acertou_numero):
        print("Você acertou :) Seu score foi de {:02d} pontos".format(pontos))
        print("Fim de jogo!!")
        break
    elif (chute_maior):
        print("Você errou! O seu chute foi maior do que o número secreto!")
        pontos = pontos - (chute - numero_secreto)
    elif (chute_menor):
        print("Você errou! O seu chute foi menor do que o número secreto!")
        pontos = pontos - (numero_secreto - chute)

# Condição caso não acerte o número
else:
    print("Fim de jogo, você não descobriu o número secreto que era: {}".format(numero_secreto))
    print("Você marcou {:02d} pontos".format(pontos))
