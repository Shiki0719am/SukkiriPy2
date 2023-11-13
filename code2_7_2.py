kokugo = input("国語の点数は？")
sannsuu = input("算数の点数は？")
rika = input("理科の点数は？")
syakai = input("社会の中点数は？")
eigo = input("英語の点数は？")
zennbu = [int(kokugo), int(sannsuu), int(syakai), int(rika), int(eigo)]
print(sum(zennbu))
print(sum(zennbu)/len(zennbu))