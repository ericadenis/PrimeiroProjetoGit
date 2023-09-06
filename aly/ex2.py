qntpess = 0
somaid = 0
somapess = 0
resposta = "sim"
while(resposta == "sim"):
    nome = input("nome:\n")
    idade = int(input('idade:\n'))
    somaid = somaid + idade
    somapess = somapess + 1
    resposta = input('deseja continuar?')
media = somaid/somapess 
print(f'a média dos alunos é {media}')