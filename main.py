Alista = ['lavar prato', 'almoçar', 'tomar banho']


def adicionar():
    tarefa_para_adicionar = input("OK, qual tarefa vc quer adicionar? : ")

    if tarefa_para_adicionar in Alista:
        aviso = input("a tarefa já existe, quer adicionar outra ? S/N: ").strip().upper()

        if aviso == 'S':
            tarefa_para_adicionar = input("OK, qual tarefa vc quer adicionar? : ")
            Alista.append(tarefa_para_adicionar)
            print('LISTA: ')
            for palavras in Alista:
                print(f"- {palavras}")
            print("=======================================")
            print("tarefa adicionada com sucesso !!!")

            
        elif aviso == 'N':
            print('entendido, fechando o processo')
            return False
                
    else:
        Alista.append(tarefa_para_adicionar)
        print('LISTA: ')
        for palavras in Alista:
            print(f"- {palavras}")
        print("=======================================")
        print("tarefa adicionada com sucesso !!!")
        print("Deseja adicionar outra ? S/N")
        escolha_usuario = input('==>   ').strip().upper()
        if escolha_usuario == 'S':
            tarefa_para_adicionar = input("OK, qual tarefa vc quer adicionar? : ")
            Alista.append(tarefa_para_adicionar)
            print('LISTA: ')
            for palavras in Alista:
                print(f"- {palavras}")
        print("=======================================")
        print("tarefa adicionada com sucesso !!!")
        
def remover():
    tarefa_para_remover = input('Qual tarefa você quer remover:  ')

    if tarefa_para_remover not in Alista:
        print('A tarefa não existe na lista, escreva denovo.')
        tarefa_para_remover = input('Qual tarefa você quer remover:  ')
        Alista.remove(tarefa_para_remover)
        print(f'A tarefa {tarefa_para_remover} foi removida com sucesso')

        while True:
            perg_continuar = input('deseja remover outra S/N;  ').strip().upper()

            if perg_continuar == 'S':
                tarefa_para_remover = input('Qual tarefa você quer remover:  ')
                Alista.remove(tarefa_para_remover)
                print(f'A tarefa {tarefa_para_remover} foi removida com sucesso')
            elif perg_continuar == 'N':
                print('entendido')
                break
    else:
        Alista.remove(tarefa_para_remover)
        print(f'A tarefa {tarefa_para_remover} foi removida com sucesso')
        while True:
            perg_continuar = input('deseja remover outra S/N;  ').strip().upper()

            if perg_continuar == 'S':
                tarefa_para_remover = input('Qual tarefa você quer remover:  ')
                Alista.remove(tarefa_para_remover)
                print(f'A tarefa {tarefa_para_remover} foi removida com sucesso')
            elif perg_continuar == 'N':
                print('entendido')
                return False


while True:
    print('LISTA DE TAREFAS')
    print('LISTA ATUAL: ')
    for palavras in Alista:
        print(f"- {palavras}")
    print('===================================================================')

    print("O QUE VOCÊ DESEJA ? A = adicionar R = remover S = sair")
    escolha_usuario = input('==>   ').strip().upper()

    if escolha_usuario ==  'A' or escolha_usuario == 'a':
        adicionar()
    elif escolha_usuario == 'R' or escolha_usuario == 'r':
        remover()
    elif escolha_usuario == 'S' or escolha_usuario == 's':
        break
    else:
        print('escolha errada')
