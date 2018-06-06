class Animal:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("何かの動物の鳴き声")
        

class Cat(Animal): # Animalを継承
    def bark(self):
        print(self.name, "は'にゃー'と鳴く")
        
class Dog(Animal):
    def bark(self):
        print(self.name, "は'わんわん'と鳴く")
        
def bark(someone):
    someone.bark()
    
alist = [Dog("ポチ"), Cat("みけ")]
for a in alist:
    bark(a)
    

        