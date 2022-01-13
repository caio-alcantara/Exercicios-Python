def leiaArquivo(text):
    """
    -> Lê um arquivo de texto e escreve na tela, de maneira formatada, as linhas desse arquivo de texto.
       Criado para a leitura apenas do arquivo 'pessoas.txt'.
    :param text: Nome do arquivo em formato txt. Ex: leiaArquivo('pessoas.txt')
    :return: As linhas do arquivo de texto
    """
    arquivo = ''
    idade = media = 0
    try:
        arquivo = open(text, 'r')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            idade += int(dado[1])
            media += 1
            print(f'{dado[0]:<35}{dado[1]:>3} anos')
    except IndexError:
        print("A lista está vazia.")
    finally:
        arquivo.close()
    if media > 0:
        print(f"A média de idade das pessoas cadastradas é de {idade/media:.1f} anos.")


def escreveArquivo(nome, idade):
    """
    -> Abre um arquivo de texto e escreve, sem apagar os dados anteriores, o input do usuário.
    :param nome: Nome que será adicionado ao arquivo de texto.
    :param idade: idade que será adicionada ao arquivo de texto.
    :return: None
    """
    arquivo = open('pessoas.txt', 'at')
    arquivo.write(f"{nome};{idade}\n")
    print(f"Registro de {nome} adicionado com com sucesso.")
    arquivo.close()


def head(text):
    """
    -> Escreve um texto em formatação de cabeçalho.
    :param text: O texto que se deseja formatar
    :return: None
    """
    print('-=' * 22)
    print(f'{text:^44}')
    print('-=' * 22)


def menu(text):
    """
    -> Escreve um menu com as opções do parâmetro text.
    :param text: As opções que o menu terá
    :return: None
    """
    head("MENU PRINCIPAL")
    contador = 1
    for c in text:
        print(f"\33[33m{contador}\33[m - \33[34m{text[contador - 1]}\33[m")
        contador += 1
    print('-=' * 22)


def escolha():
    """
    -> Faz o usuário escolher entre três opções (1, 2, ou 3), validando a entrada de dados.
    :return: A opção escolhida
    """
    menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    choice = 0
    while True:
        try:
            choice = int(input("\33[32mOpção: \33[m"))
            if choice > 3 or choice == 0:
                print(f"\33[31mNão existe opção {choice}. Digite outro valor.\33[m")
                continue
        except (ValueError, TypeError):
            print("\33[31mValor digitado é inválido. Digite outro valor: \33[m")
            continue
        except KeyboardInterrupt:
            print("O usuário decidiu não digitar os valores.")
        break
    return choice


def arquivoExiste(text):
    """
    -> Verifica se um arquivo txt existe ou não.
    :param text: Nome do arquivo txt.
    :return: Retorna False caso o arquivo não exista, e True caso exista.
    """
    try:
        a = open(text, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(text):
    """
    -> Cria um novo arquivo txt.
    :param text: Nome do arquivo txt.
    :return: None
    """
    try:
        a = open(text, 'wt+')
        a.write('Nome:                               Idade:')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo.")
    else:
        print(f"Arquivo {text} criado com sucesso.")