#PassWord Generator
import random

print("Welcome to your Password Generator!")

randomCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

#Take the number of wanted passwords and convert to integer
numberOfPasswords = input('Please input the number of passwords to generate: ')
convertedNumberOfPasswords = int(numberOfPasswords)

#Takes the number of characters and convert to integer
numberOfCharacters = input('Please enter the number of characters wanted for each Password: ')
convertedNumberOfCharacters = int(numberOfCharacters)

print("\nGenerated Passwords: ")
print("---------------------")

#Nested for loop first creates the amount of passwords as empty strings
#Then adds in the number of random characters in to the strings and prints them out.
for password in range(convertedNumberOfPasswords):
    passwords = ''
    for characters in range(convertedNumberOfCharacters):
        passwords += random.choice(randomCharacters)
    print(passwords)
    

