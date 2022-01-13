def leia_dinheiro(text):
    valid = False
    while valid is False:
        entrada = str(input(text)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f"\033[7mERRO! '{entrada}' não é um valor válido.\033[m")
        else:
            valid = True
            return float(entrada)
