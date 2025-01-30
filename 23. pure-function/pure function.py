#functional programming: map, filter, zip, reduce
my_list = [1,2,3]
for item in my_list:
  print(item*2)

#append multiply 2
my_list = [1,2,3]
final_list=[]
for item in my_list:
  final_list.append(item*2)
print(final_list)

#multiple 2 in the new list
my_list = [1,2,3]
final_list=[]
def multiply_by2():
  for item in my_list:
    final_list.append(item*2)
multiply_by2() 
print(final_list)

# map
my_list = [1,2,3]
def multiply_by2(item):
  return item*2
print(list(map(multiply_by2, my_list)))

#filter odd numbers
my_list = [1,2,3]
def only_odd(item):
  return item % 2 != 0
print(list(filter(only_odd, my_list)))
print(my_list)

#zip                                 
my_list = [1,2,3]
your_list = {10,20,30}
her_list = [40,50,60]
print(list(zip(my_list, your_list, her_list)))

#reduce
my_list = [1,2,3]
from functools import reduce
def accumulator(acc,item):
  return acc+item
print(reduce(accumulator, my_list,0))
print(my_list)

