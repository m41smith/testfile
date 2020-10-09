import time
import random

def main():
    response = ""
    while response.lower() != 'yes':
        response = input("Wil you be my friend?")
    print("Hooray! we will be friends forever")
    number_of_times = random.randint(3,15)
    for creepy in range (number_of_times):
        print("and ever..")
        time.sleep(1)

main()