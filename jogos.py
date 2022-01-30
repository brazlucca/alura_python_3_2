import forca
import adivinhacao

def escolhe_jogo():
    print("**********************************")
    print("**Bem vindo a Jogos em Python 3!**")
    print("**********************************")

    print()
    print("(1) Forca, (2) Adivinhação")

    jogo = int(input("Escolha um jogo: "))

    if (jogo == 1):
        print("Iniciando jogo de forca")
        print()
        forca.jogar()
    elif (jogo == 2):
        print("Iniciando jogo de adivinhação")
        print()
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()