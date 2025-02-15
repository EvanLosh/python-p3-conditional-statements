#!/usr/bin/env python3

def admin_login(username='', password=''):
    if (username.upper() == "ADMIN" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    if temperature < 65:
        return "It's a little chilly out there!"
    if temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    fizz = num % 3 == 0
    buzz = num % 5 == 0
    if fizz and buzz:
        return 'FizzBuzz'
    if fizz:
        return 'Fizz'
    if buzz:
        return 'Buzz'
    else:
        return num

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
