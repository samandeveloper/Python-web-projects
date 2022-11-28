#Find duplicate numbers in the below list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#for a list without duplicate numbers
# print(list(set(some_list)))

duplicate = []
for item in some_list:
    if some_list.count(item) > 1:
      if item not in duplicate:
        duplicate.append(item)
print(duplicate)