
def cree(n : int, d :int) -> tuple[int,int] :
    if d == 0 :
        raise ZeroDivisionError()
    return (n,d)

def reduire(r : tuple[int,int] ) -> tuple[int,int] :
    pass

def pgcd(u : int,v : int) -> int :
    u = abs(u)
    v = abs(v)
    while(v != 0) :
        u,v = v, u % v
    return u

def test_pgcd() -> None :
    x = 24
    y = 36
    print(f"pgcd({x},{y}) = {pgcd(x,y)}")

if __name__ == '__main__':
    test_pgcd()

