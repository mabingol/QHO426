class Person:  #This will be our Parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
y = Person("Alex", "Green")
#x.printname()
#y.printname()

class Student(Person):
  def __init__(self, fname, lname, enyear, gradyear):
    #pass
    #Person.__init__(self, fname, lname)
    super().__init__(fname, lname)
    self.enrolyear = enyear
    self.graduationyear = gradyear

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.enrolyear)

  def graduat(self):
    print("Dear", self.firstname, self.lastname, "your graduation will be on", self.graduationyear)
  
std1 = Student("Mike", "Redhat", 2018, 2023)
#std1.printname()
#print(std1.enrolyear)
#print(std1.graduationyear)
std1.welcome()
std1.graduat()
