#Computing GC Content
from collections import Counter

arquivo = open("/content/rosalind_gc (5).txt", "r")
df = arquivo.read()

if ">" in df:
  df = df.split(">")

for seq in df:
  gc = seq.count('G') + seq.count('C')
  total = len(seq)
  print(gc, total)
