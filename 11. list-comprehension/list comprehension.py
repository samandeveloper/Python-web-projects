# Duplicate code before using list comprehension

some_list = ['a','b','c','b','d','m','n','n']
duplicates =[]
for value in some_list:
  if some_list.count(value)>1:
    if value not in duplicates:
      duplicates.append(value)
print(duplicates)

#Duplicate code after using list comprehension>>we use set to omitt duplication of duplicate
some_list = ['a','b','c','b','d','m','n','n']
duplicates =list(set([value for value in some_list if some_list.count(value)>1 ]))
print(duplicates)