'''
Como fiz

peso = int(input('Qual o total de peso dos peixes?(Kg) '))
excesso = 0
multa = 0

if peso > 50:
    excesso = int(peso - 50)
    multa = int(excesso*4)
else:
    excesso = int(0)
    multa = int(0)

print('Você ultrapassou %.2f Kg, e deve pagar R$ %.2f de multa'%(excesso,multa))
'''

#Como foi feito no video

peso = float(input('Peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0

print ('Multa de R$ %.2f' %multa)
print ('Excesso: %.2f' %excesso)
