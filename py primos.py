num = int(input("Digite o ultimo numero de sua lista: "))
#definição de variavel com interação usuário
total = 0
for i in range(1, num + 1):
#operação contador para numero primo
    if num % i == 0:
        print('\033[33m, ', end='')
        #mostrar com destaque de cor, os numeros que foram divisíveis
        total += 1
    else:
        print('\033[m , ', end='')
        print('{}'.format(i), end='')
        #comando para mostar a lista dos numeros
print('\nO numero {}  foi divisivel {} vezes'.format(num, total))
#comando para mostrar a quantidade de vezes que o numero foi divisísel
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
#comando IF e ELSE para determinar se o numero é primo ou não
