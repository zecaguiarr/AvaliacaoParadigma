ListaOriginal = [7, 5, 3, 9, 6, 4, 1]
Tarefa1 = [7, 5, 3, 9, 6, 4, 1]
Soma = 0
NovaLista = []

substituir = 5
remover = 4
for x in range(len(Tarefa1)):
    if (Tarefa1[x] == 9):
        Tarefa1.insert(x, substituir)
        Tarefa1.pop(x+1)

for x in range(len(Tarefa1)):
    if(x == remover):
        Tarefa1.pop(x+1)

NovaLista = Tarefa1


for x in NovaLista:
    Soma += x

print('Essa é a lista original:', ListaOriginal)
print('Essa é a nova lista:', NovaLista)
print('Essa é a soma dos valores da nova lista:', Soma)
