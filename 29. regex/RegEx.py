#using re module in regular expressions
import re
string='search inside of this text please'
text=re.search('this',string)
print(text)

#methods
print(text.span())
print(text.start())
print(text.end())
print(text.group())

#advanced : just add the pattern line
import re
pattern=re.compile('please')
string='search inside of this text please'
text=pattern.search(string)
print(text.group())

import re
pattern=re.compile('search inside of this text please')
string='search inside of this text please 12'

#in fullmatch method, the pattern and the string must be exact same
text1=pattern.fullmatch(string)
text2=pattern.findall(string)

#in match method, the pattern and the string should be similar not the exact same
text3=pattern.match(string)
print(text1)
print(text2)
print(text3)

#using regex signs
import re
pattern=re.compile(r"([a-zA-Z]).([a])")
string='search inside of this text please'

#search the whole string
text=pattern.search(string)
print(text.group())
print(text.group(1))
print(text.group(2))