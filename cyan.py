"""Cyan's password generator"""
name = input()
surname = input()
age = input()
if len(name) >= 5 and len(surname) >= 5:
    print(name[:2], surname[-1], age[-1], sep="")
else:
    print(name[0], age, surname[-1], sep="")
