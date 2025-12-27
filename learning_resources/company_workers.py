''' Create something that will assign level of access to people 
that have that given  job role, via sub classes. 
'''
class employee: 
    def __init__(self, firstname, lastname, job_role):
        self.firstname = firstname
        self.lastname = lastname
        self.job_role = job_role
    
    def __str__(self):
        return '\n {} {} {}'.format(self.firstname, self.lastname, self.job_role)
    
class manager(employee):
    def __init__(self, firstname, lastname, job_role, access_level):
        super().__init__(firstname, lastname, job_role)
        self.access_level = access_level
    
    def __str__(self):
        return '{} {}'.format(super().__str__(), self.access_level)

class assistant(employee): 
    def __init__(self, firstname, lastname, job_role, access_level):
        super().__init__(firstname, lastname, job_role)
        self.access_level = access_level
    
    def __str__(self):
        return '{} {}'.format(super().__str__(), self.access_level)

emp1 = manager('John', 'Smith', 'Manager', 'Level 5')
emp2 = assistant('John', 'Smith', 'Manager', 'Level 1')


# print(emp1.access_level)
# print(emp2.access_level)
print(emp1)
print(emp2)