#Email Validation using regex
import re
pattern=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# insert your email in the below line:
string='b@b.com'	
text=pattern.search(string)
print(text)
if (text):
  print ("Valid Email")
else:
  print ("Email not valid")


