import json
import random
import jsonpickle
from model import Noeud,Composant,Circuit

def testJson(obj) :
    print(f"------ original object : -----------")
    print(f"type : {type(obj)}")
    print(obj)
    jobj = json.dumps(obj)
    print(f"------ json representation : ----------\n{jobj}")
    objAgain = json.loads(jobj)
    print(f"------ reload : ----------")
    print(f"type : {type(objAgain)}")
    print(objAgain)


def testDict() :
    print("le package json est parfaitement adapté pour sauvegarder des dictionnaires")
    dict = {'a' : 10 , 'b' : [10,'toto']}
    testJson(dict)

class ClassSimple():
    def __init__(self):
        self._a = 10
        self._b = "coucou"

    def __str__(self):
        return f"[ClassSimple a={self._a} b= {self._b}]"

class ClassSimple():
    def __init__(self):
        self._a = 10
        self._b = "coucou"
def testClassSimple(obj) :
    print("on peut utiliser simplement le package json pour sauvegarder les attributs d'une classe")
    print("en utilisant l'attribut spécial __dict__")
    dictofcs = obj.__dict__
    testJson(dictofcs)
    print("mais après relecture, on obtient un dict, pas un objet de la classe")

class ReferenceCirculaire1 :
    def __init__(self,c2 : 'ReferenceCirculaire2'):
        self._pseudoId = random.random()
        self._refToC2 = c2
        c2._refToC1 = self

    def __str__(self):
        return f"[C1 {self._pseudoId}]"


class ReferenceCirculaire2 :
    def __init__(self):
        self._pseudoId = random.random()

    def __str__(self):
        return f"[C2 {self._pseudoId}]"


def testClassAvecDependanceCirculaire() :
    c2 = ReferenceCirculaire2()
    c1 = ReferenceCirculaire1(c2)
    try :
        testClassSimple(c1)
    except :
        print("ERREUR : le package json de base de gère pas les références circulaires, ni même les attributs de type classe")


def testAvecJsonPickle(obj) :
    print(f"------ original object : ---------")
    print(f"type : {type(obj)}")
    print(obj)
    jobj = jsonpickle.encode(obj)
    print(f"------ jsonpickle representation : ----------\n{jobj}")
    objAgain = jsonpickle.decode(jobj)
    print(f"------ reload : ----------")
    print(f"type : {type(objAgain)}")
    print(objAgain)

def testClassAvecJsonPickle() :
    c2 = ReferenceCirculaire2()
    c1 = ReferenceCirculaire1(c2)
    testAvecJsonPickle(c1)

def testCompletSurCircuit() :
    c1 = Circuit.circuit_test()
    testAvecJsonPickle(c1)

if __name__ == '__main__':
    print("============ test dictionnaire avec package de base json ====================")
    testDict()
    print("============ test classe avec package de base json ====================")
    testClassSimple(ClassSimple())
    print("============ test classe dépendance récursive ==> problème avec package json de base ====================")
    testClassAvecDependanceCirculaire()
    print("============ test classe avec package jsonpickle ====================")
    testClassAvecJsonPickle()
    print("============ test classe circuit avec package jsonpickle ====================")
    testCompletSurCircuit()