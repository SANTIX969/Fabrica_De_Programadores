lista_de_usuario = ["Ana", "Leo", "João"]
senha_de_usuario = ["Ana123", "L30", "j0Ao"]

usuario = input("Digite se usuario...\n")
senha = input("Digite sua senha...\n")

index_nome = lista_de_usuario.index(usuario)
index_senha = senha_de_usuario.index(senha)

if index_nome == index_senha:
    print("Login Bem-Sucedido")

else:
    print("Falha No Login")
