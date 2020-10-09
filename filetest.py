
import random

def main():
    file = open("silly.txt", "r")
    all_of_file = file.readlines()
    counter = 1
    for line in all_of_file:
        if counter%2 == 1:
            print(line)
        else:
            pass
        counter += 1


def reverser():
    rev_file = open("Reversable.txt", "r")
    all_lines = rev_file.readlines()
    to_reverse = all_lines[1]
    backwards = ""
    for char in to_reverse:
        backwards = f"{char}{backwards}"
    print(f"reversing string gives you {backwards}")


def string_formating_demo():
    result = 100/3
    formatted_number = "{:5.3f}".format(result)
    print(f"the result is {formatted_number}")


#main()
reverser()
#string_formating_demo()