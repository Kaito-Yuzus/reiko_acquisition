''' Create something that will assign level of access to people 
that have that given  job role, via sub classes. 
'''
class employee: 
    def __init__(self, name, lastname, job_role):
        self.name = name
        self.lastname = lastname
        self.job_role = job_role
    
    def __str__(self):
        return '\n {} {} {}'.format(self.name, self.lastname, self.job_role)
    
    def manager(employee): 

    
    

        


emp1 = employee('John', 'Smith', 'Manager')
emp2 = employee('Bob', 'Jones', 'Assisant')

print(emp1)