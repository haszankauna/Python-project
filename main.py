import time

name = input("Input Your Name: ")
datetime = input("Input what time did you come to class: ")

while True:
    now = datetime.datetime.now().time()
    if now.hour == 8 and now.minute == 00:
        success = True
        print("Welcome to class!")
