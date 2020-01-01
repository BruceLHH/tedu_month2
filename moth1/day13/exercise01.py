class Animal:
    def sound(self):
        print ("I can speak.")

class Dog(Animal):
    def run(self):
        print ("I can run.")

class Bird(Animal):
    def flay(self):
        print("i can flaying.")

dog = Dog()
niao = Bird()
dog.sound()
niao.sound()
niao.flay()

print (isinstance(dog,Animal))
print (isinstance(dog,Dog))
print (isinstance(dog,Bird))
print (isinstance(Animal,Bird))
print()
print (issubclass(Dog,Animal))
print (issubclass(Dog,Bird))
print (issubclass(Animal,Bird))