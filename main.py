from defs import *

def main():
    chances = 3
    frase = "polkadot academy"
    blank_frase = progress = blank_get(frase)
    chute_certo = []
    chutes_totais = []
    print(f"\nSua oração até o momento é:\n\n{blank_frase}\n\nPrepare-se para o jogo!")

    while chances >= 0:

        chute = guess_get(chutes_totais)
        chutes_totais.append(chute)

        if guess_check(chute, frase):
            print(f"\nVocê acertou! A letra {chute} faz parte da oração.")
            chute_certo.append(chute)
            progress = update_progress(frase, chute_certo)
        else:
            print(f"\nVocê errou! A letra {chute} não faz parte da oração.\nVocê perdeu uma tentativa.")
            chances -= 1

        print(f"\nSeu progresso atual é:\n\n{progress}\n")
        print(f"VIDAS RESTANTES: {chances}\nLETRAS USADAS: {chutes_totais}")

        if progress == frase:
            print(f"\nVocê venceu!!")
            break
    else:
        print("\nVocê perdeu...")
        print(f"A oração correta era '{frase.capitalize()}'\n")

if __name__ == "__main__":
    main()