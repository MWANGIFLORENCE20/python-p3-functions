#!/usr/bin/env python3


def greet_programmer():
    print("Hello, programmer!")
    return greet_programmer

greet_programmer()

def greet(name="Guido"):
    print(f"Hello, {name}!")
    return greet 

greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    return greet_with_default

greet_with_default()

def add(num1=45, num2=55):
    print("added numters")
    return num1 + num2

add()    


def halve(number=50):
    return number / 2

halve()
    
