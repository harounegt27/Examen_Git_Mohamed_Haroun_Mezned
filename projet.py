def somme(T):
    S = 0
    for t in T:
        S += t
    return S

Data = [1, 2, 3]
if Data:
    print("La somme est : ",sum(Data))
    print("Le min est : ",min(Data))
    print("Le max est : ",max(Data))
else:
    print("Liste vide")


