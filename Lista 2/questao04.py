n1=int(input('1º número: '))
n2=int(input('2º número: '))
n3=int(input('3º número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é %d' %n1)
    else:
        print('O maior número é %d' %n3)
elif n2 > n3:
    print('O maior número é %d' %n2)
else:
    print('O maior número é %d' %n3)

'''
Como Foi resolvido no video

a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))

if a>= b and a >= c:
    print ('Primeiro: %d' %a)
elif b >= c:
    print ('Segundo: %d' %b)
else:
    print ('Terceiro: %d' %c)
'''


