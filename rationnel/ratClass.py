def pgcd(u : int,v : int) -> int :
    u = abs(u)
    v = abs(v)
    while(v != 0) :
        u,v = v, u % v
    return u


class Rationnel :

    def __init__(self,num : int = 0,denom : int = 1):
        if denom == 0 :
            raise ZeroDivisionError("dénominateur nul")
        self.num = num
        self.denom = denom

    def add (self,r2 : 'Rationnel') -> 'Rationnel' :
        print("je sais pas faire")

    def __str__(self) -> str:
        return f"rat : {self.num}/{self.denom}"

if __name__ == '__main__':
    r1 = Rationnel()
    print(r1)
    r2 = Rationnel(23)
    print(r2)
    r3 = Rationnel(23,2)
    print(r3)
    r4 = Rationnel(denom=12)
    print(r4)
    r1.add(r2)
