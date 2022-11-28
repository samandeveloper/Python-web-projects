# In this project we will use "Twilio API" for sending SMS
from twilio.rest import Client
account_sid ='your code'
auth_token = '[AuthToken]'
client = Client(account_sid,auth_token)
message = client.messages.create(
	from_='+1XXXXXXXXXX', #cellphone number that sends SMS
	to='+1XXXXXXXXXX' #cellphone number that you want to receive SMS
	)
print(message.sid)