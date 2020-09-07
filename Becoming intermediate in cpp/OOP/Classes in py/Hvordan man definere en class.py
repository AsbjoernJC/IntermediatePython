#Classes are a great way of creating a user defined data structure consisting of storing multiple data types, properties of a single object. 
#While a list could be used to accomplish the same
#Classes can be easier to manage, as you don't need to remember indexes, and they can be easier maintainable

#Classes define functions called methods (just like modules have their own data structure with their own methods, probably built from classes? (V))
#a class is a blueprint, creating criterias (age, name, etc.) that must be had to define what the class is aiming to describe eg. a dog. 
#An instance is an object built from a class, this would be the object holding the data of the dog, so the age, name etc. It's an actual real example.

#A class always begins with the class keyword. User defined objects are mutable by default
class Dog:      #classes are used to represent an object, a person, a car etc. consisting of multiple properties. Python class names use a CapitalizedWords notation
    # Class attributes. Theyh have the same value for all class instances. 
    species = "Canis familiaris"        #class attributes are defined directly beneath the class 
    def __init__(self, name, age):  #the function _ _ init _ _(parameters) is a function that describes the properties that this class must be described by
        #so first and foremost it must always be itself, self (dog in this case). The dog objects must also have a name and an age.
        self.name = name    #creates an attribute called name and assigns it to the value of the name parameter. can later on be called by Dogobject.name
        self.age = age      #creates an attribute called age and assigns it to the value of the age parameter. can later on be called by Dogobject.age
        #attributes created in __init__() are called instance attributes. All Dog objects will have values for name and age, but they will be dynamic
        #everytime a new dog object is created __init__() sets the initial state of the object, by assigning the values of the objects properties.
        #__init__() initializes each new instance of the class.
    #pass        #pass is written as to not crash the code as a sort of placeholder code 

#Creating a new object from a class is called instantiating an object. Which is done by writing a new Dog object: Dog()
a = Dog("Jakob", 5) #prints: <__main__.Dog object at 0x0000021653653C40>, which is a memory address, indicating, where the Dog object is stored.
b = Dog("Jakobi", 6)
print(a)    #what is interesting is that the memory address seems to change each time the code is run
print(b)
print(a == b)   #prints false as they are stored at different memory addresses
#Using dot notation (methods) you can get the instance attributes of the Dog object
print(a.name)   #prints: Jakob, as the name of dog a was Jakob
print(b.age)    #prints: 6, as the age of Dog(b) was 6
#Using dot notation you can also get the class attributes.
print(a.species)    #prints: Canis familiaris. as the class attribute the dog was assigned was "Canis familiaris"
#This showcases one of the biggest strengths of classes: sharing all the attributes. In this case all dogs are described by: name, age
#After the attributes of a Dog object has been given they can be changed, both class -and instance attributes :
a.name = "Bonderøv"     #the instance attribute (name) of Dog object a has been changed to "Bonderøv". It's a mutable data type and could therefore be changed in place
print(a.name)   #prints: Bonderøv

#Nåede til Instance Methods

