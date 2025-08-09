#Lógica Algoritmos e Programação de Computadores
#Prof.  : Francisco Filho
#Id Al  : 2586101057
#aluno  : Joao Henrique Gomes Lima
#Turma  : EADADS3A
#Criacao: 20250805.1227


import os, json
from datetime import date



#Carregar Cardapio
with open("cardapio.json",'r',encoding="utf-8") as f:
    cardapio=json.load(f)

#Carregar Clientes
with open("clientes.json",'r',encoding="utf-8") as f:
    clientes=json.load(f)

#Carregar Pedidos
with open("pedidos.json",'r',encoding="utf-8") as f:
    pedidos=json.load(f)


#Menu Principal
def MenuPrincipal():
    print("Coffee Shops Tia Rosa")
    print()
    print("1- Fazer Pedido")
    print("2- Cardapio")
    print("3- Lista De Pedidos")
    print("4- Lista De Clientes")
    print("0- Sair")

#Pegar Proximo Pedido
def pegarProximoPedido(pedidos):
    chaves=pedidos.keys()
    numeros=[]
    for chave in chaves:
        numeros.append(int(chave))
    ultimoPedido=max(numeros)
    return ultimoPedido+1

#Item inexistente
def pegarDescItem(cardapio, numItem):
    item=cardapio.get(str(numItem))
    if item:
        nome = item.get("prodnome", "Descrição não encontrada")
        preco = item.get("preco", 0.00)
        return nome, preco
    else:
        return "Item não existe", 0.00

#Fazer Pedido
def anotarPedido(pedidos, cardapio):
    numProximoPedido = pegarProximoPedido(pedidos)
    numItem = 0
    ItensPedido = []
    totalPedido = 0.0

    print("Fazer Pedido")
    print(" Pedido:", numProximoPedido, "")
    while True:
        numItem = input("Item: ")
        if numItem == "" or numItem == "99":
            break
        descItem, precoItem = pegarDescItem(cardapio, numItem)
        print(f"\033[1A\033[10C← {descItem} - R$ {precoItem:.2f}")
        totalPedido += float(precoItem)
        ItensPedido.append(int(numItem))

    print(" Total Pedido: ", f"R$ {totalPedido:.2f}", "")

    Cliente = input(" Nome: ")
    Clientecpf  = input(" CPF: ")

    novoPedido = {
        "pedido": numProximoPedido,
        "data": date.today().strftime("%Y%m%d"),
        "clicpf": Clientecpf,
        "clinome": Cliente,
        "produtos": ItensPedido
    }

    pedidos[str(numProximoPedido)] = novoPedido

    #escrever no arquivo de pedidos
    with open("pedidos.json", "w", encoding="utf-8") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)

    print("\nPedido registrado com sucesso!")

#Cardapio
def listarCardapio(cardapio):
    print("Cardapio")
    for id_produto, dados in cardapio.items():
        nome=dados['prodnome']
        traco=' -'
        print(f"\n {id_produto} {nome}{traco} Preço: R$ {dados['preco']:.2f}")
        print(f" Ingredientes: {dados['ingredientes']}")

#Lista de Pedidos
def listarVendas(pedidos,cardapio):
    TotalDoDia=0.0;
    print("Pedidos")
    for chave in pedidos:
        pedido=pedidos[chave]
        print(f" Pedido: {pedido['pedido']}",f"Data: {pedido['data']}")
        print(f" CPF: {pedido['clicpf']},  Nome: {pedido['clinome']}")
        print(" Itens:")
        total=0.0
        for prod_id in pedido["produtos"]:
            prod=cardapio.get(str(prod_id), {})
            nome=prod.get("prodnome", "Produto não encontrado")
            preco=prod.get("preco", 0.00)
            print(f" {prod_id} - {nome:<20} {preco:>6.2f}")
            total+=preco
        print(f"{'Total:'} {total:>6.2f}")
        TotalDoDia+=total
    print(f"{'Total do dia:'} {TotalDoDia:>6.2f}")

#Lista de Clientes
def listarClientes(clientes):
    print("Clientes")
    for id_cliente, dados in sorted(clientes.items(),key=lambda item: item[1]['clinome']):
        print(f" {int(id_cliente):02} {dados['cpf']} {dados['clinome']}")

#codigo de menu
def main():
    opcao=1
    while opcao!=0:
        opcao=0
        MenuPrincipal()
        opcao=int(input(" Entrada[0]:") or 0)
        if opcao==0:
            break
        elif opcao==1:
            anotarPedido(pedidos,cardapio)
        elif opcao==2:
            listarCardapio(cardapio)
        elif opcao==3:
            listarVendas(pedidos,cardapio)
        elif opcao==4:
            listarClientes(clientes)
        print()
        input('Aperte Enter para voltar')


#rodar programa
if __name__== "__main__":
    main()
    #mensagem de finalização
    print("\n Tchau!")



