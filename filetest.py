
import random

def main():
    file = open("silly.txt", "r")
    all_of_file = file.readlines()
    random_line = random.choice(all_of_file)
    print(random_line)


def reverser():
    rev_file = open("Reversable.txt", "r")
    all_lines = rev_file.readlines()
    to_insert = all_lines[0]
    print(f"welcome to {to_insert}, fantastic student")


def string_formating_demo():
    result = 100/3
    formatted_number = "{:5.3f}".format(result)
    print(f"the result is {formatted_number}")

#reverser()
#main()
string_formating_demo()