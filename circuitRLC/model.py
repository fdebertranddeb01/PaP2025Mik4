import math

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
        return self._py

    @py.setter
    def py(self, py: float):
        self._py = py

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

    def __str__(self):
        res = ""
        res = res + "-------- Circuit RLC ------------\n"
        res = res + "-------- Noeuds\n"
        for n in self.noeuds :
            res = res + str(n) + "\n"
        res = res + "-------- Composants\n"
        for c in self.compos :
            res = res + str(c) + "\n"
        return res


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

    @classmethod
    def circuit_test(cls) -> 'Circuit':
        n1 = Noeud(0, 0)
        n2 = Noeud(0, 1)
        n3 = Noeud(1, 1)
        c1 = Generateur(n1, n2, 220)
        c2 = Condensateur(n2, n3, 0.001)
        c3 = Condensateur(n3, n1, 0.002)
        c = Circuit()
        c.add_noeud(n1)
        c.add_noeud(n2)
        c.add_noeud(n3)
        c.add_compo(c1)
        c.add_compo(c2)
        c.add_compo(c3)
        return c


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
    c = Circuit.circuit_test()
    print(c)
