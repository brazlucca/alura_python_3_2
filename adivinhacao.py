import random

def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?", numero_secreto)
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 20
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print()
        print("Tentativa:  {}  de  {}".format(rodada, total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos! Parabéns!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, o seu chuto foi maior do que o numero secreto")
            elif(menor):
                print("Você errou, o seu chuto foi menor do que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print()

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()