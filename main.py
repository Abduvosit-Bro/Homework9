class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


user = Comment('Alecco', 'Hello')
print(user.likes)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person1 = Person('John', 25, 'Male')
person2 = Person('Sarah', 35, 'Female')
person3 = Person('Bob', 42, 'Male')

print(f'Name: {person1.name}, age: {person1.age}, gender: {person1.gender}')
print(f'Name: {person2.name}, age: {person2.age}, gender: {person2.gender}')
print(f'Name: {person3.name}, age: {person3.age}, gender: {person3.gender}')