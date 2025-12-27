
class adding_num_name: 
    add_amount = 1
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def combine_names(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.age)

    def adding_num(self): 
        self.age = int(self.age + adding_num_name.add_amount)
        return self.combine_names()
    
    def adding_num2(self): 
        self.age = int(self.age + self.add_amount)
        return self.combine_names()
    
person1 = adding_num_name('John', 'Smith', 22)
person1.add_amount = 2

# Calling the class variable, unaffected by the instance changing it
print(person1.adding_num())
# Calling the instance variable, affected by the instance changing it
print(person1.adding_num2())