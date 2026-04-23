import os

password = "hardcoded_password"  # vulnerability

def login():
    user_input = input("Enter username: ")
    print("Welcome " + user_input)

login()
