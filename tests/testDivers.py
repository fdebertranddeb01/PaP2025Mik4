

a = [2,3,6,5]
carre =[x*x for x in a if x %2 == 0]
print(carre)

def ft(t1 : list[int],t2 : list) -> None :
    if t1[0] == 0 :
        t2[1] = 3
    else :
       t2[0] = t2[0] - 1
       ft(t2,t1)

def mainFt() -> None :
    t = [1,1]
    ft(t, t)
    print(f"t = {t}")

mainFt()