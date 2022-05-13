## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## person has-a name of some kind
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Satan
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## mary has-a pet, satan
mary.pet = satan

## frank is-a employee who makes $120k / yy
frank = Employee("Frank", 120000)

## rover is-a pet of frank
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## Crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()