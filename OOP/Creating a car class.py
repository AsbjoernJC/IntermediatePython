class Car:


    def __init__(self, color, mileage):
        self.color = color.lower()  #instance attributes
        self.mileage = mileage  #mileage is in miles

OleBlue = Car("Blue", 20000)
TrustyRed = Car("Red", 30000) 

for car in (OleBlue, TrustyRed):
    print("The " + car.color + " car has " + str(car.mileage) + " miles.")
#Prints: The blue car has 20000 miles.\n The red car has 30000 miles.