
def escolhe_jogo ():
    # Mensagem de boas vindas
    print("*Bem vindo ao Lobby dos jogos!*")
    print("(1) Forca (2) Adivinhação")

    # Variáveis
    jogo_escolhido = 0
    import forca
    import adivinhacao

    # Obriga jogador a escolhe um jogo disponível
    while (jogo_escolhido != 1 or jogo_escolhido != 2):
        jogo_escolhido = int(input("Escolha um jogo:  "))
        if (jogo_escolhido) == 1:
            print("Direcionando ao jogo da Forca")
            forca.jogar()
            break
        elif (jogo_escolhido) == 2:
            print("Direcionando ao jogo da Adivinhação")
            adivinhacao.jogar()
            break
        else:
            print("Escolha um jogo válido")
            print("(1) Forca (2) Adivinhação")
            continue

if (__name__ == "__main__"):
    escolhe_jogo()