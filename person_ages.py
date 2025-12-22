
class people:

    person_age = 0

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def fullname(self):
        return 'This is {} {}'.format(self.name, self.lastname)


    def set_age(self, age):
        self.person_age += age
        return self.person_age

    @classmethod
    def adding_age(cls, age):
        cls.person_age += age
        return cls.person_age       


person1 = people('John', 'Smith')
person2 = people('Tom', 'Jones')

# Instance
print('--------------------------')
print(person1.fullname())
print(person1.set_age(31))
print('--------------------------')
print(person1.fullname())
print(person1.set_age(31))
print('--------------------------')
print(person2.fullname())
print(person2.set_age(42))
print('--------------------------')
# Class
print(person1.fullname())
print(people.adding_age(31))
print('--------------------------')
print(person2.fullname())
print(people.adding_age(42))
print('--------------------------')









