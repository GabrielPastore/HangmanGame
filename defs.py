def blank_get(frase: str):
    frase_return = ""
    for letra in frase:
        if letra != " ":
            frase_return += "_"
        else:
            frase_return += " "
    return frase_return

def guess_get(chutes_totais):
    chute = input("Escolha uma letra: ").lower()[0]
    while chute in chutes_totais:
        print("\nVocê já tentou essa letra.\nEscolha outra que você ainda não tenha usado.\n")
        print(chutes_totais)
        chute = input("Escolha uma letra: ").lower()[0]
    return chute

def guess_check(chute: str, frase: str):
    return True if chute in frase else False

def update_progress(frase: str, chutes: list):
    frase_retorno = ""
    for letra in frase:
        if letra in chutes or letra == " ":
            frase_retorno += letra
        else:
            frase_retorno += "_"
    return frase_retorno