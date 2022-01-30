def jogar():
    print("**********************************")
    print("***Bem vindo ao jogo de forca!****")
    print("**********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print()
    print("Palavra secreta: ", letras_acertadas)
    print()

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6

        acertou = "_" not in letras_acertadas

        print("Palavra secreta: ", letras_acertadas)

    print()
    if(acertou):
        print("Parabéns você acertou!")
    else:
        print("Você perdeu")

    print()
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()
