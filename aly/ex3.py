total = 0
resposta = 'sim'
cor = 0
sp = 0
santos = 0
palm = 0
outro = 0
while(resposta == 'sim'):
    time = input('qual time você torce?')
    if time == 'corinthians':
        cor = cor + 1
    elif time == 'sao paulo':
        sp = sp + 1
    elif time == 'santos':
        santos = santos + 1
    elif time == 'palmeiras':
        palm = palm + 1
    else:
        outro = outro + 1
    total = total + 1
    resposta = input('deseja continuar?')
per_cor = (cor/total) * 100
per_palm = (palm/total) * 100
per_sp = (sp/total) * 100
per_santos = (santos/total) * 100
per_outro = (outro/total) * 100
print(f"corinthians: {per_cor}%")
print(f"palmeiras: {per_palm}%")
print(f"são paulo: {per_sp}%")
print(f"Santos: {per_santos}%")
print(f'Outros: {per_outro}%')