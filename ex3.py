senha = ""

while senha != "abcd":
    senha = str(input("Digite sua senha: \n"))
  
if senha != "abcd":
    print("Senha incorreta. \n")
else:
    print("Senha correta.\n")