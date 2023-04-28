import random

class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        sounds = ['크르릉', '커러렁']
        self.sound = random.choices(sounds)
        
    def speak(self):
        return f"{self.sound[0]}"
    

class Dog(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        sounds = ['멍멍멍', '왈왈왈', '끼잉끼잉']
        self.sound = random.choices(sounds)

class Cat(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        sounds = ['야아옹', '미야오', '끼야아ㅏ악']
        self.sound = random.choices(sounds)
    

bear = Animal("곰순이", 4)
dog1 = Dog("백구", 5)
dog2 = Dog("루비", 2)
cat1 = Cat("루루", 5)
cat2 = Cat("꼬미", 7)

print(bear.speak())
print(dog1.speak())
print(dog2.speak())
print(cat1.speak())
print(cat2.speak())