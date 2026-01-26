print('================= LISTAS DE TAREFAS =================')

banco_de_dados = []

def listar(banco_de_dados):
    for i, tarefa in enumerate(banco_de_dados, start=1):
        print(f'{i}. {tarefa['tarefa']}')
    



def criar_tarefa(banco_de_dados):
    nome = input('Digite a tarefa: ').strip()

    for tarefa in banco_de_dados:
        if tarefa['tarefa'] == nome:
            print('Essa tarefa já existe.')
            return

    descrição = input('digite a descrição: ')
    prioridade = input('''
    ======= PRIORIDADE =======
                        
        1 - URGENTE
        2 - ALTA
        3 - MÉDIA
        4 - BAIXA
        
        ==> ''')
    categoria = input('''
    ===== CATEGORIA =====
        
        1 - INDIVIDUAL
        2 - LAZER
        3 - TRABALHO
        4 - FILHOS
        
    ===> ''')
    
    tarefa_db = {
        'tarefa': nome,
        'descrição': descrição,
        'prioridade': prioridade,
        'categoria': categoria 
    }

    banco_de_dados.append(banco_de_dados)
    print('======= TAREFA ADICIONA A LISTA =======')
    for chave, valor in tarefa_db.items():
        print(f'{chave} == {valor}')


def excluir_tarefa(banco_de_dados):
    print('Tarefas atuais:')
    for i, tarefa in enumerate(banco_de_dados):
        print(f"{i+1} - {tarefa['tarefa']}")
    indice = int(input('Digite o número da tarefa que quer excluir: ')) - 1
    if 0 <= indice < len(banco_de_dados):
        removida = banco_de_dados.pop(indice)
        print(f"Tarefa '{removida['tarefa']}' removida com sucesso!")
    else:
        print("Número inválido.")


def modificar(banco_de_dados):
    return


#MOSTRA O MENU
def menu():
    while True:
        mostrar = input(''' 
        1 - VER TAREFAS
        2 - CRIAR TAREFA
        3 - EXCLUIR TAREFA
        4 - ALTERAR TAREFA
        5 - SAIR
        ==> ''')

        if mostrar == '1':
            listar(banco_de_dados)
        elif mostrar == '2':
            criar_tarefa(banco_de_dados)
        elif mostrar == '3':
            excluir_tarefa(banco_de_dados)
        elif mostrar == '4':
            modificar(banco_de_dados) 
        elif mostrar == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

menu()
