# importing random module to make random choice from string module 
import random
import string

#taking the letters and numbers and symbols from string module
characters=string.ascii_letters + string.digits + string.punctuation

# User input for length
length=int(input('Enter the Lemgth of the Password: '))

#Making password list by using of random module of particular length from characters
password=(random.choices(characters,k=length))

# showing the passowrd my joining the words of list of password
print(''.join(password))