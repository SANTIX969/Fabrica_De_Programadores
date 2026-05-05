print("---Instagram login---")

lista_de_usuario = ["João"]
senhas_usuario = ["18050105"]

usuario_atual = input("DIgite seu usuario: ")
senha_atual = input("Digite sua senha: ")
while True:
    if usuario_atual in lista_de_usuario and senha_atual in senhas_usuario:
        print("login bem-sucedido")
        break
else:
    print("usuario ou senha invalido")
    
    
    
    