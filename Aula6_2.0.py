lista = ["Maça", "Melancia"]

fruta = input("Digite o nome da fruta que vc quer comprar: \n")

if fruta in lista:

    
    print(f"{fruta}, sua fruta tem na feira!!!\n")

else:
    opcao = input("sua fruta nn tem na feira!!!\n\nDeseja que nós colocamos na feira? (sim/não)\n\n ").lower ()

    if opcao == "sim":
     
     novo_usuario = input ("\n Digite o nome da fruta que voce quer que seja adicionada : \n")
     lista.append(fruta)
     print("fruta adicionado na feira com sucesso!!!\n", lista)

    else:
       print("obrigado por vim a nossa feira")