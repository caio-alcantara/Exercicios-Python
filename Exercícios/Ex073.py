#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação.
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'RB Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Athlético-PH', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('=' * 80)
print("Os 5 primeiros times do Campeonato Brasileiro de 2021 são:")
print('=' * 80)
print(times[:5])
print('=' * 80)
print("Os últimos 4 colocados e, consequentemente rebaixados, são:")
print('=' * 80)
print(times[16:])
print('=' * 80)
print("Os times, sortidos em ordem alfabética, são:")
print('=' * 80)
print(sorted(times))
print('=' * 80)
print(f"A Chapecoense se encontra na {times.index('Chapecoense') + 1}ª posição.")
print('=' * 80)