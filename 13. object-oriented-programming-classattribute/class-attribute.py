
class PlayerCharacter():
  def __init__(self,name,age):
    self.name=name
    self.age=age
  # up to now, the following command lines are not needed
  def run(self):
    print('run')
    return 'done'

player1=PlayerCharacter('John',32)
player2=PlayerCharacter('Cindy',21)
player2.attack=50
print(player1.name)
print(player2.age)
print(player2.attack)
#now the run function is needed
print(player1.run())