import json
from model import Noeud,Composant,Circuit

def encodeClass(obj) -> dict :
    if isinstance(obj,JsonAble) :
        print(f"obj : {obj} ; class {type(obj)}")
        instanceSlots = obj.__dict__.copy()
        instanceSlots["__class__"] = obj.__class__
        return instanceSlots
    else :
        return obj

def testJSON(toJSon) :
    print("-------- original -------")
    print(toJSon)
    jdic = json.dumps(toJSon,default=encodeClass)
    print("-------- json -------")
    print(jdic)
    redic = json.loads(jdic)
    print("-------- relecture --------")
    print(redic)

class JsonAble:
    pass

class C1(JsonAble):
    def __init__(self):
        self._a = 10
        self._b = 'bb'

    def __str__(self):
        return f"[C1 a={self._a} b={self._b}]"

class C2(JsonAble):
    def __init__(self):
        self._c1 = C1()
        self._c = 'cc'

    def __str__(self):
        return f"[C2 c1={self._c1} c={self._c}]"

if __name__ == '__main__':
    dic = {'a': 10, 'b': [1, 2, 3], 'c': {'d': 11, 'e': 12}}
    testJSON(dic)
    c2 = C2()
    testJSON(c2)

