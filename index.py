escolha=0
lista=[]

while escolha !="0":
  print("Menu")
  print("0 - Fim")
  print("1 - Cadastro de Produtos")
  print("2 - Lista de Produtos")
  print("3 - Confirmação do Produto")
  print("4 - Total")
  escolha = input("Escolha uma opção:")
  if escolha == 0:
    escolha = input("Tem certeza que quer finalizar o programa? 0 - Sim , 5 - Não")
  if escolha == 1:
    print("Cadastrando produto")
    produto = input("Escolha o nome do produto:")
    quantidade = input("Escolha a quantidade do produto:")
    

  if escolha=="2":
    print("Exibindo produtos...")
    contador=0
    for produto in lista:

      print(contador,"#",produto[0]," ",produto[1],"-",produto[2])
      contador=contador+1
  if escolha=="3":
    print("Confirmando produto...")
    posicao=input("Digite a posição do produto:")
    posicao_int=int(posicao)
    preco=input("Digite o preco do "+lista[posicao_int][1] +":")
    lista[posicao_int][0]="OK"
    lista[posicao_int][3]=preco
  if escolha=="4":
    print("Mostrando Todos Produtos...")
    print("Produtos que não foram comprados...")
    contador=0
    for produto in lista:
      if produto[0]=="":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
    print("Produtos que foram comprados...")
    contador=0
    precototal=0
    for produto in lista:
      if produto[0]=="OK":
        print(contador,"#",produto[0]," ",produto[1],"-",produto[2], "R$", produto[3])
        contador=contador+1
        precototal=precototal+int(produto[2])*float(produto[3])
    print("Preco Total: R$",precototal)


print("Fim do programa!")

carrinho = []
print("""
Menu
0 - Finalizar programa
1 - Cadastra produto
2 - Ver carrinho
3 - Confirma produto
4 - Ver total
0 - sair
""")

escolha = input('Escolha uma opção')

while escolha != 0:
    if escolha == 1:
        item = input('Entre com um produto')
        if item in carrinho:
            print('Produto já está no carrinho:')
            x = int(input('Deseja mudar a quantidade? 1 para sim, 2 para não:'))
            if x == 1:
                novaquantidade = int(input('Informe a nova quantidade do produto:'))
                item = 0
                quantidade = novaquantidade
                input(item)
        else:
            quantidade = int(input("Entre a quantidade:"))
            carrinho.append(item)


    if escolha == 2:
        print("Exibindo produtos...")
        contador = 0
        for item in carrinho:
            print(contador,item,":",quantidade)
            contador = contador + 1

    if escolha == 3:
        posicao = int(input(f'Digite a posição do item'))
        posicao_int = int(posicao)
        preco = input(f"Digite o preço do produto {carrinho[posicao_int][1]}")
        carrinho[item] = "OK"
        carrinho[posicao][3] = preco
    escolha = int(input("Escolha uma opção"))

else:
   print("Programa encerrado")
   
   carrinho = []

# cria e adiciona batatas ao carrinho
item = {'nome': 'batatas', 'quantidade': 1}
carrinho.append(item)
print("\nO carrinho tem: ")
print(carrinho)

# cria e adiciona arroz ao carrinho
item = {'nome': 'arroz', 'quantidade': 10}
carrinho.append(item)
print("\nO carrinho tem: ")
print(carrinho)

# mostra a quantidade de batatas
for item in carrinho:
  if item['nome'] == 'batatas':
    print("\nQuantidade de batatas no carrinho: ")
  	print(item['quantidade'])

# procura o arroz e atualiza a quantidade para 10
for item in carrinho:
	novo_item = item
    if novo_item['nome'] == 'arroz':
		novo_item['quantidade'] = 10
	novo_carrinho.append(novo_item)
carrinho = novo_carrinho
print("\nO carrinho tem: ")
print(carrinho)

# procura as batatas e atualiza cria uma nova propriedade 'sabor'
for item in carrinho:
	novo_item = item
	if novo_item['nome'] == 'batatas':
  		novo_item['sabor'] = 'ketchup'
	novo_carrinho.append(novo_item)
carrinho = novo_carrinho
print("\nO carrinho tem: ")
print(carrinho)

carrinho = []

print("""
Menu
0 - Finalizar programa
1 - Cadastra produto
2 - Ver carrinho
3 - Confirma produto
4 - Ver total
5 - Mudar quantidade do produto
0 - sair
""")

escolha = input('Escolha uma opção')

while escolha != 0:
    if escolha == 1:
        item = input('Entre com um produto')
        if item in carrinho:
            print('Produto já está no carrinho:')
            nova_quantidade = int(input('Digite a nova quantidade:'))
            novo_produto = produto
            produto = {'nome': item, 'quantidade': nova_quantidade}

        else:
            quantidade = int(input('Digite a quantidade do produto:'))
            produto = {'nome': item, 'quantidade': quantidade}
            carrinho.append(produto)
