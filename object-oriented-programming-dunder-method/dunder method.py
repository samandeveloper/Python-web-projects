class Toy():
  def __init__(self,color,age):
    self.color=color
    self.age=age

    self.my_dict={
      'name':'Yoyo',
      'has_pets':'False'
    }

  #__str__ method
  def __str__(self):
    return f'{self.color}'

  #__len__ method
  def __len__(self):
    return 5

  #__del__method
  def __del__(self):
    print('deleted!')

  #__call__ method
  def __call__(self):
    return('yes?')

  #__getitem__method
  def __getitem__(self,i):
    return self.my_dict[i]

action_figure=Toy('red',0)

#str
print(action_figure.__str__())
#or
print(str(action_figure))

#len
print(len(action_figure))
del >>bayad bedone print bashad
del(action_figure)

#call
print(action_figure())

#getitem
print(action_figure['name'])