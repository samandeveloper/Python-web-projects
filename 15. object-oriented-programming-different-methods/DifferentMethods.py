class PlayerCharacter:
  def __init__(self,name,age):
    self.name=name
    self.age=age

#1.Instance Method
  def shout(self):
    print(f'my name is {self.name}')

#2.Class Method
  @classmethod
  def adding_things(cls,num1,num2):
    return num1+num2
    # return cls('Teddy', num1+num2)

#3.Static Method
  @staticmethod
  def adding_things2(num1,num2):
    return num1+num2
# player1=PlayerCharacter('John',32)
# print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things2(2,3))
print(PlayerCharacter('John',32).adding_things2(3,3))


