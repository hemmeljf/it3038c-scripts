# Final Project - Jake Hemmelgarn

This script will generate a password for you and also check to make sure that it is strong enough.

I think this is a practical script because some people may have trouble coming up with passwords. This script is a quick way for people to get strong, safe passwords where they can then record in a safe spot. The strength test helps verify that the password is of good quality.


I used the below sites as guides:

  -  https://hackr.io/blog/python-projects (Number 13 and 6)

I ran this script in powershell using python finalproject.pys


This will generate the password and print out what it is.
```
import secrets
import string
import time

def create_pass(pass_length=14):
	letters = string.ascii_letters
	digits = string.digits
	special_chars = string.punctuation
	
	alpha = letters + digits + special_chars
	pwd = ''
	pass_strong = False
	
	while not pass_strong:
		pwd = ''
		for i in range(pass_length):
			pwd += ''.join(secrets.choice(alpha))
			
		if (any(char in special_chars for char in pwd) and
				sum(char in digits for char in pwd) >=3):
			pass_strong = True
			
	return pwd
	
##Print Password and Check
if __name__ == '__main__':
	gen_password = create_pass()
	print("Your generated password is:", gen_password)

```

Now we will check the strength of the password.

Here is the code that runs the strength test.
```
##Password Strength Check

print('Now lets check the strength of the password!')

def is_pass_strong(password):
	##wait 5 seconds to check the password
	print("Checking...")
	time.sleep(5)

	##Check is passwordhas 10 characters
	if len(password) < 10:
		return False
		
	## Uppercased
	if not any(char.isupper() for char in password):
		return False
		
	## Lowercase
	if not any(char.islower() for char in password):
		return false
		
	## Digits
	if not any(char.isdigit() for char in password):
		return False
		
	## Special Character
	special_chars = string.punctuation
	if not any(char in special_chars for char in password):
		return False
		
	return True


if __name__ == '__main__':	
	if is_pass_strong(gen_password):
		print("Your password meets the strength requirments!")
	else:
		print("Your password does not meet the strength requirements.")
			
```

Congrats! You now have a new password that is strong enough! 
Please do not share this with other people!





