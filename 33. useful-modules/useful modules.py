#collections module
from collections import Counter,defaultdict,OrderedDict

#Counter
li=[1,2,3,4,5,6,7,7]
print(Counter(li))
sentence='sam sam sam'
print(Counter(sentence))

#defaultdict
# dictionary={
#   'a':1,
#   'b':2
# }
# print(dictionary['f'])

dictionary=defaultdict(float,{
  'a':1,
  'b':2
})
print(dictionary['c'])

dictionary=defaultdict(lambda:5,{
  'a':1,
  'b':2
})
print(dictionary['c'])

dictionary=defaultdict(lambda:'does not exit',{
  'a':1,
  'b':2
})
print(dictionary['c'])

#OrderedDict
d1=OrderedDict()
d1['a']=1
d1['b']=2

d2=OrderedDict()
d2['a']=1
d2['b']=2
print(d1==d2)

#datetime module
import datetime
print(datetime.time())
print(datetime.time(5,45,2))
print(datetime.date.today())

#array
from array import array
arr=array('i',[1,2,3])
print(arr)
print(arr[0])