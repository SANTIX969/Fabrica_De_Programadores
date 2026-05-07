lista = [' Carlão o Padeiro, Vanessa,João '] # lista de cadastro de pessoas 

Usuario = input('Digite seu usuario: \n') # usuario 
print('------INICIO------ \n') # inicio
if Usuario in lista: #Usuario
     print('login bem-sucedido!!! \n') # deu bom
     
else:
     print(f'Usuario {Usuario} não exeste!!! \n') # usuario
     print('-----FIM------') # fim 
     