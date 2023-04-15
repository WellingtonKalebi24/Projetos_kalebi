import random

def jogar():

    print("********************************")
    print("Bem Vindo ao jogo de Adivinhação")
    print("********************************")

    #variaveis#
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Define o nível: "))

    #nivel dificuldade#
    if(nivel == 1):
        total_de_tentativas= 20
    elif(nivel == 2):
        total_de_tentativas= 10
    else:
        total_de_tentativas = 5

    #quantidade que pode ser jogada e chute pode ser apenas 1 até 100#
    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

    #condicao se acertou ou nao, se passou perto do numero corresp./ tirada de pontos#
        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos


    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()