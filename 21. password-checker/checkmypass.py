#In this incredable code, we can import any password as we want, so it will check and show us how many times the mentioned password hacks
#first install request module.The requests module allows you to send HTTP requests using Python
import requests
import hashlib	#hashlib module:hash the password
import sys

def request_api_data(query_char):
	url ='https://api.pwnedpasswords.com/range/'+ query_char	#using k-anonymity technique and just 5 first character of hash password
	res = requests.get(url)
	# print(res)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching:{res.status_code},check the api and try again')
	else:
		return res	


def get_password_leaks_count(hashes,hash_to_check):
	hashes=(line.split(':') for line in hashes.text.splitlines())	#anything in a line will be splited
	for h,count in hashes:
		if h==hash_to_check:
			return count
	return 0
		# print(hashes,count)

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #the whole hash password
	first5_char, tail = sha1password[:5], sha1password[5:]
	# first5_char = sha1password[:5]
	# tail = sha1password[5:]
	response = request_api_data(first5_char)
	print(first5_char,tail)
	print(response)
	return get_password_leaks_count(response, tail)

# request_api_data('123')

# pwned_api_check('agf')

def main(args):
	for password in args:	#we can give multiple passwords
		count=pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times..you should probably change your password')
		else:
			print(f'{password} was NOT found. Carry on!')
	return 'done!'
if __name__=='__main__':
	main(sys.argv[1:])	
