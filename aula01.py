op = 0
teatro = 0
cadeiras = []
totReservas = 0
totEspetaculo = 0
totQtReservas = 0
totQtVendidas = 0
totVendidas = 0
while True:    
    op = int(input('''
[1] - Iniciar o teatro
[2] - Reservar lugar
[3] - Comprar lugar
[4] - Liberar lugar
[5] - Listar poltronas
[6] - Encerrar o espetáculo
[7] - Reiniciar o espetáculo
Escolha uma opção:
'''))
    if op == 1:
        if teatro == 0:
            linhas = int(input("Informe a quantidade de linhas: "))
            while linhas > 300:
                print("Quantidade informada maior que o permitido")
                linhas = int(input("Informe a quantidade de linhas: ")) 
            colunas = int(input("Informe a quantidade de colunas: "))
            while colunas > 300:
                print("Quantidade informada maior que o permitido")
                colunas = int(input("Informe a quantidade de colunas: "))
            ingresso = float(input("Qual o valor do ingresso: R$ "))
            cadeiras = [['Livre' for _ in range(colunas)] for _ in range(linhas)]
        else:
            print("O teatro já foi iniciado")
        teatro = 1

    elif op == 2:

        linha = int(input("Informe a linha: "))
        coluna = int(input("Informe a coluna: "))

        if linha > linhas or coluna > colunas:
            print("Esse lugar não existe")
        else:
            linha -= 1
            coluna -= 1
            if cadeiras[linha][coluna] == 'Livre':
                cadeiras[linha][coluna] = 'Reservado' 
                totQtReservas += 1
                totReservas += ingresso * 0.3
                totEspetaculo += ingresso * 0.3
                print("Lugar reservado")
                print(cadeiras)
            else:
                print('Este lugar está reservado. Escolha outra cadeira.')

    elif op == 3:
        
        linha = int(input("Informe a linha: "))
        coluna = int(input("Informe a coluna: "))

        if linha > linhas or coluna > colunas:
            print("Esse lugar não existe")
        else:
            linha -= 1
            coluna -=1
            if cadeiras[linha][coluna] == 'Livre':
                cadeiras[linha][coluna] = 'Vendido'
                totQtVendidas += 1
                totVendidas += ingresso
                totEspetaculo += ingresso
                print('Lugar comprado')
                print(cadeiras)
            elif cadeiras[linha][coluna] == 'Reservado':
                cadeiras[linha][coluna] = 'Vendido'
                totQtReservas -= 1
                totQtVendidas += 1
                totVendidas += ingresso * 0.7
                totEspetaculo += ingresso * 0.7
                print("Lugar reservado")
                print(cadeiras)

    elif op == 6:
        totCadeiras = linhas * colunas
        if totQtVendidas > totCadeiras * 0.6 + 1:
            print('Total Geral de Cadeiras: {}'.format(totCadeiras))
            print('Total de Cadeiras Vazias: {}'.format(linhas * colunas - totQtVendidas))
            print('Total de Cadeiras Reservadas: {}'.format(totQtReservas))
            print('Total de Cadeiras Vendidas: {}'.format(totQtVendidas))
            print('Total do Espetáculo em R$: {}'.format(totEspetaculo))
            break