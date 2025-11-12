from pickletools import long1


class Truc:
    def __init__(self):
        self._chose = 3

    @property
    def chose(self) -> int:
        return self._chose

    @chose.setter
    def chose(self,val : int) -> None:
        self._chose = val

    def __str__(self):
        return f"[Truc {self.chose}]"

def testDirect():
    c1 = Truc()
    c2 = c1
    c2.chose = 4
    print(f"c1 = {c1} ; c2 = {c2}")

def testDansList():
    c1 = Truc()
    l1 = [c1,c1]
    l2 = l1
    c1.chose = 4
    print(f"l1 = {" ".join(map(str,l1))} ; l2 = {" ".join(map(str,l2))}")

if __name__ == '__main__':
    testDirect()
    testDansList()