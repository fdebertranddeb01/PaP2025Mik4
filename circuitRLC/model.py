import math

from shiboken6.Shiboken import Object


class Noeud :
    def __init__(self,px : float,py : float):
        self._px = px
        self._py = py
        self._compos_dep = []
        self._compos_arr = []

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

    @property
    def compos_dep(self):
        return self._compos_dep

    @property
    def compos_arr(self):
        return self._compos_arr

    def ajoute_compo_dep(self,compo : 'Composant') -> None:
        self._compos_dep.append(compo)

    def ajoute_compo_arr(self,compo : 'Composant') -> None:
        self._compos_arr.append(compo)

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
    def __init__(self,ndep : 'Noeud',narr : 'Noeud'):
        self._ndep = ndep
        self._narr = narr
        ndep.ajoute_compo_dep(self)
        narr.ajoute_compo_arr(self)

    @property
    def ndep(self):
        return self._ndep

    @property
    def narr(self):
        return self._narr


class Generateur(Composant) :
    def __init__(self,ndep : 'Noeud',narr : 'Noeud',fem : float):
        super().__init__(ndep,narr)
        self._fem = fem

    @property
    def fem(self):
        return self._fem

    @fem.setter
    def fem(self,fem : float):
        self._fem = fem

    def __str__(self):
        return f"[Generateur : {self.fem} V ; de {self.ndep} vers {self.narr}]"




class Condensateur(Composant) :
    def __init__(self,ndep : 'Noeud',narr : 'Noeud',capacite : float):
        super().__init__(ndep,narr)
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
        return f"[Condensateur : {self.capacite*1000000} microF ; de {self.ndep} vers {self.narr}]"

class Circuit:
    def __init__(self):
        self._noeuds = []
        self._compos = []

    @property
    def noeuds(self):
        return self._noeuds

    @property
    def compos(self):
        return self._compos

    def add_noeud(self,n : 'Noeud') -> None :
        self._noeuds.append(n)

    def add_compo(self,c : 'Composant') -> None:
        if c.ndep not in self._noeuds :
            raise Exception("compo avec noeud hors circuit")
        if c.narr not in self._noeuds :
            raise Exception("compo avec noeud hors circuit")
        self._compos.append(c)

    def positionNoeud(self,n : 'Noeud') -> int :
        """ renvoie la position du noeud dans la liste des noeuds
        raise un exception si le noeud n'est pas dans le circuit"""
        return self._noeuds.index(n)

    def positionCompo(self,c: 'Composant') -> int :
        """ renvoie la position du composant dans la liste des composants
        raise un exception si le composant n'est pas dans le circuit"""
        return self._compos.index(c)


def test2() :
    n0 = Noeud(0,0)
    n1 = Noeud(1, 1)
    n2 = Noeud(2,2)
    c1 = Condensateur(n1,n2,10)
    g1 = Generateur(n0,n1,220)
    print(isinstance(c1,Composant))
    print(c1)
    print(g1)


if __name__ == '__main__':
    # test1()
    test2()
    print([1,2,3].index(4))
