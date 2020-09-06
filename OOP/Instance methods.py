class Dog:     
    species = "Canis familiaris"  

    def __init__(self, name, age): 
        self.name = name    
        self.age = age      

    #def description(self):  #This is an instance method. instance methods are functions that always
        #have the parameter self, just like __init__. Unlike init the parameters aren't a necessisty
        #to describe a dog. An instance method can only be called from an instance of that class.
    def __str__(self):
        return(self.name + " is " + str(self.age) + " years old.")

    def speak(self, sound):     #Also an instance methods. This one has two parameters
        #self, and sound. Where sound would an argument passed as a string
        #otherwise the concetanation below wouldn't work
        return(self.name + " says: '" + sound + "'")    #can also just use print
        #will alow you to just call the instance methods and get the output without print func

a = Dog("Jakob", 5) 
b = Dog("Jakobi", 6)

print(a.speak("Jeg lever 7 gange så kort som mennesker"))   
#print(a.description())

#it's good practice to have a instance method that returns a string containing useful information
#about the instance object (eg. dog a)

print(a)    #Prints: <__main__.Dog object at 0x0000027C6D263C40>
#this shows where the object is stored in memory. It can be changed with a special instance
#method called __str__()

#cause of the changes (def description(self)) was commented out. print(a) now returns:
#Jakob is 5 years old.

#methods like __init__() and __str__() are called dunder methods. As they begin and end with
#double underscores. There are many more than these two
