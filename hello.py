awal=input ('input nilai awal')
akhir=input ('input nilai akhir')

awal= int (awal)
akhir= int (akhir)


print('==== Looping ====')
while (awal<=akhir):
    total=awal * 10000
    print(str(awal)+'Liter Bensin='+str(total))

    awal=awal+1
