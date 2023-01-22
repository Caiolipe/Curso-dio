menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''
saldo = (0)
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Depósito')
        valor = float(input('Entre com um valor: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            print(saldo)
            print('Deposito efetuado com sucesso!')
        if valor <= 0:
            print('Não e possivel adicionar valores abaixo de 1!')


    elif opcao == 's':
        print('Saque')
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        
        elif excedeu_limite:
            print('Operação falou! o valor do saque excede o limite')

        elif excedeu_saques:
            print('Operação falhou! Número maximo de saques excedido')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! o valor informado é invalido') 

   
    elif opcao == 'e':
        print('\n ====================== EXTRATO ======================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('========================================================')    
    elif opcao == 'q':
        break
    
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')