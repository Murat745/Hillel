"""
Lesson 14, homework 10, task 1 solution.
Godzzilla Class.
"""


class UnexpectedTypeException(Exception):
    pass


class Godzilla:
    def __init__(self, stomach_space=100):
        self.stomach_space = stomach_space

    def eat(self, human_volume):
        self.stomach_space -= human_volume
        if human_volume < 0:
            raise UnexpectedTypeException("Human volume must be positive!")
        elif self.stomach_space <= 10:
            print("AGGRRRRHHH!!! Can't eat anymore!!!")


godzzilla = Godzilla()
godzzilla.eat(50)
godzzilla.eat(10)
godzzilla.eat(30)  # AGGRRRRHHH!!! Can't eat anymore!!!
