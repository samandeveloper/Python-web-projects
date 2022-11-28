#Object Oriented Programming-Inheritance
#Parent class
class User(object):
  def __init__(self,email):
    self.email=email
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self,name,power,email): #email ra ezafe kardim
    User.__init__(self,email)
    self.name=name
    self.power=power
  def attack(self):
    print(f'attacking with power of {self.power}')

wizard1=Wizard('Merlin',50,'merlin@gmail.com')
print(wizard1.sign_in())
print(wizard1.email)



