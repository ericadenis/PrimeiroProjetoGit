fat = 1
numero = int(input('digite um número\n'))
for i in range(1, numero + 1):
    fat = fat * i
print(f"{numero}! = {fat}")