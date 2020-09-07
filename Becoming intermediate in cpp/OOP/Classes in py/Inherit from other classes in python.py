class Dog:     
    species = "Canis familiaris"  

    def __init__(self, name, age): 
        self.name = name    
        self.age = age      

    def __str__(self):
        return(self.name + " is " + str(self.age) + " years old.")

    def speak(self, sound):
        return(self.name + " barks: '" + sound + "'")    
#Creating a child class. a class that inherits from it's parent class
class JackRussellTerrier(Dog):
    def speak(self, sound = "Arf"): #changes to an instance method in child classes. Polymorphism calling the same function that's in the parent class.
        #but with a different block of code. Also known as method overriding. Used when the method in the parent class doesn't really fit the 
        #child class/sub class
        #overwrites the instance method from the parent class
        print(self.name + " says " + sound)    #uses format from child class as super() isn't called
        print(super().speak(sound))     #accessing the parent class from inside a method of a class
        #by using super(). using super() will include all of the changes to the syntax of .speak
        #created in the parent class Dog


class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

#Child classes inherit all of the instance methods and attributes and class attributes
print(miles.species)
print(miles.age)
print(type(jack))   #type(classobject) will determine the class of the object: <class '__main__.Bulldog'>
#Finding out if it's also an instance in the Dog class:
print(isinstance(miles, Dog))   #isinstance(object, class) returns bool True or False. 
#True as miles is instantiated in Dog
miles.speak()    #prints: Miles says Arf\n Miles barks: 'Arf' from parent class
#(as it is in the child class JackRusselTerrier)

#the method .speak can still be passed strings
miles.speak("Grrrrr")    #prints: Miles says Grrrrr\n Miles barks: 'Grrrrr'
