
class adding_num_name: 
    add_amount = 1
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def combine_names(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.age)

    def adding_num(self): 
        self.age = int(self.age + self.add_amount)
        return self.combine_names()

person1 = adding_num_name('John', 'Smith', 22)

print(person1.adding_num())