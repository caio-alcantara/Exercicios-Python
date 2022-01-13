cores = ['\033[m',
         '\033[0;30;41m',
         '\033[0;30;42m',
         '\033[0;30;42m',
         '\033[0;30;43m',
         '\033[0;30;44m',
         '\033[0;30;45m',
         '\033[7m'
         ]


def titulo(msg, cor=0):
    print(cores[cor], end='')
    print('~' * (len(msg) + 4))
    print(f"  {msg}")
    print('~' * (len(msg) + 4))
    print(cores[0], end='')



def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO/BIBLIOTECA {com}', 4)
    print(cores[7])
    help(com)
    print(cores[0], end='')


# Programa Principal
continuar = ''
while continuar != 'fim':
    titulo('SISTEMA DE AJUDA PYTHON', 2)
    continuar = str(input("Comando ou biblioteca > ")).strip().lower()
    ajuda(continuar)
titulo('FINALIZANDO PROGRAMA', 1)