clients = []

def add():
    clientes = []
    nome = input("digite o nome do cliente:")
    email = input("digite o e-mail do cliente:")
    clientes.append(nome)
    clientes.append(email)
    if clientes not in clients:
            clients.append(clientes)
            print("Cadastrado com sucesso!!")
    else:
            print("Cliente ja cadastrado!!")
    print(clients)

def search():
    print(clients)
    nome = input("Digite o nome do cliente:")
    for x in clients:
       if nome in x:
           print("Nome:", x[0], "\nE-mail:", x[1])

def delete():
     print(clients)
     nome = input("Digite o nome do cliente:")
     for x in clients:
         if nome in x:
             clients.remove(x)
     for y in clients:
        print("Nome:", y[0], " E-mail:", y[1],"\n")

def prints():
    cliente = []
    for cliente in clients:
        print("Nome:", cliente[0]," E-mail:", cliente[1],"\n")

def main():
    count = 0
    while True:
        print("\nEscolha a opção que deseja")
        print("1 - Adicionar clientes")
        print("2 - Buscar cliente por nome")
        print("3 - Excluir cliente")
        print("4 - Listar clientes")
        print("0 - Finalizar programa")
        opcoes = int(input())
        if opcoes < 0 or opcoes > 4:
            print("Opção inválida!!!")
        else:
            count = opcoes
        if opcoes == 1:
            add()
        if opcoes == 2:
            search()
        if opcoes == 3:
            delete()
        if opcoes == 4:
            prints()
        if opcoes == 0:
            print("FALOU JOVEMM!!")
            break

main()