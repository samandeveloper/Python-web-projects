#password Validation using regex
import re
pattern=re.compile(r"[A-za-z0-9$%#@]{8,}\d")
#insert your password in the below line:
password='jhfgdfgdg$%#7'	
check=pattern.fullmatch(password)
print(check)
if (check):
  print ("Valid Password")
else:
  print ("Invalid Password")



