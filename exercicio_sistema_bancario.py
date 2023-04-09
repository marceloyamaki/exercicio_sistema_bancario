from datetime import datetime

menu = """
Selecione operação:
[s] Saque
[d] Depósito
[e] Extrato
[x] Sair do sistema"""


limite=500
saldo=1000
extrato=['Saldo'.ljust(11)+'R$'+str(saldo).ljust(8)]

opcao=''
while True:
    print(menu)
    opcao=input().lower()
    if opcao=='s':
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
        n_saques=0
        for linha in extrato:
            if data_e_hora_em_texto[0:10]==linha[21:31]:
                n_saques+=1
        if n_saques>=3:
            print('Limite de 3 saques diários')
        else:
            print('Saque')
            valor=int(input("Digite valor do saque:"))
            while valor>500 or valor>saldo:
                if valor>500:
                    print("Valor máximo de saque: R$500")
                    valor=int(input("Digite valor do saque:"))
                elif valor>saldo:
                    print("Saldo insuficiente: R$"+str(saldo))
                    valor=int(input("Digite valor do saque:"))                    
            saldo-=valor
            extrato[0]='Saldo'.ljust(11)+'R$'+str(saldo).ljust(8)
            extrato.append('Saque'.ljust(11)+'R$'+str(valor).ljust(8)+data_e_hora_em_texto)
    
    elif opcao=='d':
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
        print('Deposito')
        valor=int(input("Digite valor do depósito:"))
        saldo+=valor
        extrato[0]='Saldo'.ljust(11)+'R$'+str(saldo).ljust(8)
        extrato.append('Depósito'.ljust(11)+'R$'+str(valor).ljust(8)+data_e_hora_em_texto)
    
    elif opcao=='e':
        print('*******************Extrato*******************')
        if len(extrato)>1:
            for linha in extrato[::-1]:
                if 'Saldo' in linha:
                    print('---------------------------------------------')
                    print(linha)
                else:
                    print(linha)            
        else:
            print(extrato[-1])
        print('*********************************************')
    
    elif opcao=='x':
        print('Sair do sistema')
        break
    
    else:
        print('Opção inválida')