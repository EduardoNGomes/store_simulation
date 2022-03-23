t1 = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Arroz', 4.5, 'Paçoca', 0.5, 'Pamonha', 5.4)
soma = 0

print('-'*30)
print()
print('-'*9, 'CARDAPIO', '-'*11)
print()
print('-'*30)

for v,i in enumerate(t1):
    if v % 2 == 0:
        print(f'{i:<7}',end=' ')
        print('.........',end=' ')
    else:
        print(f'R$: {i:>}')
print('-'*30)

while True:
    user_shop = str(input('Qual item voce deseja comprar? ')).capitalize()
    if user_shop in t1:
        item = t1.index(user_shop)+1
        soma += t1[item]
        print('\033[32mObjeto computado\033[m')
    else:
        print('\033[31mOpcao invalida\033[m')
    

    while True:
        user_answer = str(input('Deseja continuar? ')).strip()[0]
        if user_answer in 'SsNn':
            break
        elif user_answer not in 'SsNn':
            print('\033[31mOpcao invalida\033[m')
    if user_answer in 'Nn':
        break

print(f'A soma total dos objetos comprados foi de: R$ {soma:>.2f}.')