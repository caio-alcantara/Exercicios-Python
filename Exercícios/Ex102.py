# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado 'show',
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def factorial(num, show=False):
    """
    * Calcula o fatorial de um número n.
    :param num: O número que terá o seu fatorial calculado
    :param show: Define se o processo do cálculo será ou não exibido (True ou False)
    :return: Retorna o fatorial do número n
    """
    fatorial = 1
    for c in range(num, 0, -1):
        fatorial *= c
        if show is True:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f'\33[7m{fatorial}\33[m'


# Programa Principal
digito = int(input("De qual número desejas ver o fatorial? "))
detalhamento = str(input("Deseja ver o cálculo detalhado? [S/N] ")).strip().upper()
mostrar = False
while detalhamento != 'S' and detalhamento != 'N':
    detalhamento = str(input("Opção inválida! Deseja ver o cálculo detalhado? [S/N] ")).strip().upper()
if detalhamento == 'S':
    mostrar = True
print(f"O fatorial do número {digito} é:")
print(factorial(digito, mostrar))
