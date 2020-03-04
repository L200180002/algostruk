def jumlahHurufKonsonan(x):
    total = 0
    vocal = ["a","i","u","e","o"]
    for i in x:
        if i in x :
            if i in vocal:
                total+=1
    return [len(x), len(x)-total]

i=jumlahHurufKonsonan("satria")

print(i)
