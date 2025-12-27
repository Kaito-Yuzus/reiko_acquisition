class car: 
    def __init__(self, num_doors, color, brand):
        self.num_doors = num_doors
        self.color = color
        self.brand = brand

    def to_string(self):
        return '{num_doors} {current_color} {the_brand}'.format(num_doors = self.num_doors, current_color = self.color, the_brand =  self.brand)
        # return '{} {} {}'.format(self.num_doors, self.color, self.brand)
        # Same as the code above, assigns based on order
car1 = car(4, 'red', 'ford')
print(car1.to_string())
