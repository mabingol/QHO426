"""
class MyClass:
  x = 5

  
p1 = MyClass()
print(p1.x)


class Person:
  def __init__(self, name, age):
    self.age = age
    self.name = name
p1 = Person("John", 36)

print(p1.name)
print(p1.age)


print("Type", type(p1))
print("Dir ", dir(p1))
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print(self.age)

p1 = Person("John", 36)

p1.myfunc()


"""

class PartyAnimal:
  x = 0

  def party(self) :
    self.x = self.x + 1
    print("So far",self.x)

an = PartyAnimal()

print("Type", type(an))
print("Dir ", dir(an))

"""

