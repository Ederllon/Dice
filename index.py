
from random import randint
while True:
    print(50*'-')
    pointDice = int(input('Qual pontuação máxima do dado? '))
    print('')
    numDice = int(input('Quantos dados você quer rodar? '))
    print(50*'-')
    for count in range(0,numDice):
        print('')
        print("dado {} : {}" .format((count+1),randint(1,pointDice)))
    print('')    
    cont=str(input('Quer continuar ou parar o programa?[S/N] ')).upper().strip()
    
    if cont in 'Ss':
        print('')
    elif cont in 'Nn':
        print('')
        print('Programa finalizado')
        print('')
        break
        
            
