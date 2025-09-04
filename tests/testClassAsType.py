
class Truc() :

    # toujours une erreur en python 3.13 !!
    # def chose(self,p2 : Truc):
    def chose(self, p2: 'Truc'):

            print("coucou")

t = Truc()
t.chose(t)
