#Complementing a Strand of DNA
arquivo = open("/content/rosalind_revc (1).txt", "r")
df = arquivo.read()

df = df[::-1]

complement = df.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()

print(complement)
