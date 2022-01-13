def metade(num=0, formatar=False):
    res = num / 2
    if formatar is True:
        return moeda(res)
    else:
        return res


def dobro(num=0, formatar=False):
    res = num * 2
    if formatar is True:
        return moeda(res)
    else:
        return res


def aumentar(num=0, aumento=0, formatar=False):
    res = num + (aumento/100 * num)
    if formatar is True:
        return moeda(res)
    else:
        return res


def reduzir(num=0, reducao=0, formatar=False):
    res = num - (reducao/100 * num)
    if formatar is True:
        return moeda(res)
    else:
        return res


def moeda(valor=0):
    return f"R${valor:.2f}".replace('.', ',')


def resumo(valor=0, aumento=0, redução=0):

    print('=' * 45)
    print(f'{"RESUMO DO VALOR":^45}')
    print('=' * 45)

    print(f"{'Preço analisado:':<30} {moeda(valor)}")
    print(f"{'O dobro do preço:':<30} {dobro(valor, True):}")
    print(f"{'A metade do preço:':<30} {metade(valor, True)}")
    print(f"{f'{aumento}% de aumento:':<30} {aumentar(valor, aumento, True)}")
    print(f"{f'{redução}% de redução:':<30} {reduzir(valor, redução, True)}")
    print('=' * 45)