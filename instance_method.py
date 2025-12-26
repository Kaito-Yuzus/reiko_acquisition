class add_1:

    start_value = 1

    def __init__(self, input):
        self.input = input

    def add_num(self): 
        self.start_value += self.input
        return self.start_value        

attempt1 = add_1(2)
attempt2 = add_1(60)

print('---')
print(attempt1.add_num())
print('---')
print(attempt1.add_num())
print('---')
print(attempt2.add_num())
print('---')
print(attempt1.add_num())
print('---')