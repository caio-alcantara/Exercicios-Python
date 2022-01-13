expr = str(input("Digite uma expressão numérica/algébrica: "))
parenteses = []
for s in expr:
    if s == '(':
        parenteses.append('(')
    elif s == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print("Sua expressão é válida.")
else:
    print("Sua expressão não é válida.")
