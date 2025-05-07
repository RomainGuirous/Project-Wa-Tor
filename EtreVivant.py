from random import randint


class EtreVivant:

    est_vivant = True

    def __init__(self, position, age=0):
        self._position = position
        self._age = age

    @property
    def position(self):
        return self._position

    def se_deplacer(self):

        directions_possibles = (
            "NSOE"  # création string des directions (Nord, Sud, Ouest, Est)
        )
        direction = directions_possibles[randint(0, 3)]  # une direction au hasard
        if direction == "N":
            self._position = (self._position[0], self._position[1] + 1)
        if direction == "S":
            self._position = (self._position[0], self._position[1] - 1)
        if direction == "O":
            self._position = (self._position[0] + 1, self._position[1])
        if direction == "E":
            self._position = (self._position[0] - 1, self._position[1] + 1)

    @property
    def age(self):
        return self._age

    def se_reproduire():
        pass

    def s_alimenter():
        pass

    def vieillir(self):

        self._age += 1

    def __repr__(self):
        # merci Benjamin <3
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
