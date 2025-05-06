from random import randint

class EtreVivant:

    est_vivant = True

    def __init__(self, position, age = 0):
        self.__position = position
        self.__age = age

    @property
    def position(self):
        return self.__position

    def se_deplacer(self):
        
        directions_possibles = "NSOE" # création string des directions (Nord, Sud, Ouest, Est)
        direction = directions_possibles[randint(0,3)] # une direction au hasard
        if direction == "N":
            self.__position = (self.__position[0], self.__position[1] + 1)
        if direction == "S":
            self.__position = (self.__position[0], self.__position[1] - 1)
        if direction == "O":
            self.__position = (self.__position[0] + 1, self.__position[1])
        if direction == "E":
            self.__position = (self.__position[0] - 1, self.__position[1] + 1)

    @property
    def age(self):
        return self.__age

    def se_reproduire():
        pass

    def s_alimenter():
        pass

    def mourir(est_vivant):

        if not est_vivant:
            del self

    def vieillir(self):

        self.__age += 1

    def __repr__(self):
        # merci Benjamin <3
        attrs = ', '.join(f"{key}={value!r}" for key,value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

poisson_test = EtreVivant((1,10))
print(repr(poisson_test))
# poisson_test.vieillir()
# poisson_test.vieillir()
# print(poisson_test.age)
