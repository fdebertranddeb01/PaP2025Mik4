
def cree(n : int, d :int) -> tuple[int,int] :
    if d == 0 :
        raise ZeroDivisionError()
    return (n,d)

def pgcd(u : int,v : int) -> int :
    u = abs(u)
    v = abs(v)
    while(v != 0) :
        u,v = v, u % v
    return u

def reduire(r : tuple[int,int] ) -> tuple[int,int] :
    p = pgcd(r[0],r[1])
    return (r[0]/p,r[1]/p)


def test_pgcd() -> None :
    x = 24
    y = 36
    print(f"pgcd({x},{y}) = {pgcd(x,y)}")

def add(r1 : tuple[int,int], r2 : tuple[int,int]) ->  tuple[int,int] :
    nn = r1[0] * r2[1] + r2[0] * r1[1]
    nd = r1[1] * r2[1]
    return reduire((nn,nd))

if __name__ == '__main__':
    r1 = (24,36)
    r2 = (1,2)
    s = add(r1,r2)
    print(f"somme : {s}")

