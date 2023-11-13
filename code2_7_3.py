matuda = {1,2,3,4,5}
asagi = {3,4,5,6,"7",}
input("心の準備が出来たらEnterキーを押してください")
kekka = int(len((matuda & asagi))/len((matuda | asagi))*100)
print(f"相性は{kekka}%")

