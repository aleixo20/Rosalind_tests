#Transcrição
arquivo = open("/content/rosalind_rna (1).txt", "r")
df = arquivo.read()
print('DNAseq', df)
print('RNAseq', df.replace('T', 'U'))
