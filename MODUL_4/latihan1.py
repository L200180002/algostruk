def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return print("targetnya terdapat di array itu.")
    return print("targetnya tidak terdapat di array itu.")
