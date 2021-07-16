nome = 'Lucas Quintela'

print(nome, len(nome))



# while i < len(nome):
#     print(nome[i])
#     i += 1
#

for i in range(len(nome)):
    print(nome[i])

for i, c in enumerate(nome):
    if c == 'a':
        break
    print(i, nome)

