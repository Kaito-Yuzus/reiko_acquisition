class car: 
    def __init__(self, num_doors, color, brand):
        self.num_doors = num_doors
        self.color = color
        self.brand = brand

    def to_string(self):
        return '{} {} {}'.format(self.num_doors, self.color, self.brand)
         
print(car(4, 'red', 'ford').to_string())