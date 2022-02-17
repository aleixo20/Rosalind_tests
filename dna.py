from collections import Counter

arquivo = open("/content/rosalind_dna (1).txt", "r")

for i, frase in enumerate(lista):
   lista2 = list(frase)
   
contagem = Counter(lista2)
print(contagem.most_common())
