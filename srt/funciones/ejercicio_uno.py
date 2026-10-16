#crear un programa que permita desarollar las 4 operaciones (suma,resta,devicion ,multiplicacion)



def operaciones((n:list,o:str)):
    if o=="+":
        return sum(n)
print(operaciones([4,8,20,78],"+"))