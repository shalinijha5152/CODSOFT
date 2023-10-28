# Password Generator using python

# import string and random module to generate password
import string
import random

if __name__ == '__main__':

    # defining the characters to be used in password
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    # Ask user to give password length
    password_length = int(input("Enter password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # shuffling the characters to create a strong password
    random.shuffle(s)

    # print the pssword
    print("Your password is: ")
    print("".join(s[0:password_length]))