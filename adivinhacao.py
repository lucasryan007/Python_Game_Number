#Mensagem de Boas Vindas :)
print("* Bem vindo ao jogo de Adivinhação *")

#Variáveis
numero_secreto = 42
chute_str= input("Digite o seu número: ")
chute = int(chute_str)
acertou_numero = numero_secreto == chute
errou_numero = numero_secreto < chute

#Funções
if(acertou_numero):
    print("Você acertou!!!!!!")
elif (errou_numero):
        print("Você errouuu! O seu chute foi maior do que o número secreto")
else:
        print("Você errouuu! O seu chute foi menor do que o número secreto")
print("Fim de jogo")
