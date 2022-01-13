# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request

try:
    on = urllib.request.urlopen("http://pudim.com.br/").getcode()
    print("O site está acessível a partir deste computador.")
except urllib.error.URLError:
    print("O site não está acessível a partir deste computador.")
