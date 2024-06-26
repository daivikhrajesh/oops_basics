class Person:
    number_of_ppl = 0

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod      #decorator
    def number_of_ppl_(cls):
        return cls.number_of_ppl

    @classmethod
    def add_person(cls):
        cls.number_of_ppl += 1

p1 = Person('Jimmy')
#print(p1.number_of_ppl)

p2 = Person('Jill')
#print(p1.name,p2.name)
#print(p2.number_of_ppl)

print(Person.number_of_ppl_())