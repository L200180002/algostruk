def jumlahHurufVokal(x):
    total = 0
    vokal = ["a","i","u","e","o"]
    for k in x:
        if k in vokal:
            total+=1
    return [len(x),total]

x=jumlahHurufVokal("satria")
print (x)
