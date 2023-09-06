qntpar = 0
qntimpar = 0
for i in range(0,2000):
    if i%2 == 0:
        qntpar = qntpar + 1
    else:
        qntimpar = qntimpar + 1
print(f"{qntpar} são pares e {qntimpar} são impares")