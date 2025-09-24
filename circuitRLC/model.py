import math

from shiboken6.Shiboken import Object


class Noeud :
    def __init__(self,px : float,py : float):
        self._px = px
        self._py = py

    @property
    def px(self):
        return self._px

    @px.setter
    def px(self, px: float):
        self._px = px

    @property
    def py(self):
        return self._px

    @py.setter
    def py(self, px: float):
        self._px = px

    def __str__(self):
        return f"({self.px},{self.py})"

    def distance(self,x : float,y : float) -> float:
        dx = self.px - x
        dy = self.py - y
        return math.sqrt(dx*dx + dy*dy)

    def distance_noeud(self,n2 : 'Noeud') -> float:
        return self.distance(n2.px,n2.py)

def test1() :
    n1 = Noeud(0,0)
    print(f"distance : {n1.distance(1,1)}")
    n2 = Noeud(2,3)
    print(f"distance {n1}-{n2} : {n1.distance_noeud(n2)}")

class Composant :
    pass

class Generateur(Composant) :
    pass

class Condensateur(Composant) :
    def __init__(self,capacite : float):
        if capacite < 0 :
            raise Exception("capacite négative : n'importe quoi !!")
        self._capacite = capacite

    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self,capacite : float):
        if capacite < 0 :
            raise Exception("capacite négative : n'importe quoi !!")
        self._capacite = capacite

    def __str__(self):
        return f"[Condensateur : {self.capacite*1000000} microF]"

def test2() :
    g1 = Generateur()
    print(isinstance(g1,Composant))
    o1 = Object()
    print(isinstance(o1,Composant))


if __name__ == '__main__':
    # test1()
    test2()