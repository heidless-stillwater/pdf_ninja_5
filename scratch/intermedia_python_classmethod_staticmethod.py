# static & class methods
from icecream import ic


# classmethod & staticmethod
class Person(object):
    population = 50

    def __init__(self, name='new name', age=20):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        ic(self.name, 'is ', str(self.age), ' years old')


ic(person.getPopulation())
newPerson = Person('tim', 18)
newPerson.display()
ic(newPerson.getPopulation())
ic(Person.isAdult(21))

