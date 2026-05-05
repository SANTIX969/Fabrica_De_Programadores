saldo = 1500
opcao = input("Digite 1 para saque:\n\nDigite 2 para deposito: ")

if opcao =="1":

    print(f"O saldo atual e: {saldo}")

    saque = int(input("Quanto deseja sacar? \n "))
    saldo = saldo - saque

    print(f"O saldo atual e: {saldo}")

elif opcao == "2":
    Deposito = int(input("Quanto deseja depositar? \n "))
    saldo = saldo + Deposito
   
    print(f"O saldo atual e: {saldo}")

else:
    print("Opção invalida...\nObrigado por usar nossos serviços....")