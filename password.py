import random
import string

def password():
    global length
    length=int(input("Enter the length of the password : "))
    if length<8:
        print("Password length should contain atleast 8 characters")
        password()

def inputs():
      print("Please choose either 'yes' or 'no'.")
      upper=input("Do you need uppercase leters in your password? :").lower()=='yes'
      lower=input("Do you need lowercase leters in your password? :").lower()=='yes'
      digits=input("Do you need digits in your password? :").lower()=='yes'
      special=input("Do you need special characters in your password? :").lower()=='yes'

      if not(upper or lower or digits or special):
        print("Please select atleast one option as 'yes' to generate your password.")
        inputs()


      char=""

      if upper:
       char+=string.ascii_uppercase
      if lower:
       char+=string.ascii_lowercase
      if digits:
       char+=string.digits
      if special:
       char+=string.punctuation
      password1="".join(random.choice(char) for i in range(length))
      print("Password generated is : ",password1)
      


#driver code
password()
inputs()
