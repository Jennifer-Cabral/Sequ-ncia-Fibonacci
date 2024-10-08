numero = int(input('Digite numero para gerar a sequência de Fibonnaci :'))

v1 = 1
v2 = 1
count = 0

lista = [0,1,1]

for vic in range(0, numero):
    count = v1 + v2
    v1 = count
    v2 = (count - v2)
    lista.append(count)
print(lista)

if(numero in lista):
    print('\n O número {} pertence sequência de Fibonacci'.format(numero))
else:
    print('\n O número {} não pertence na sequência de Fibonacci'.format(numero))


