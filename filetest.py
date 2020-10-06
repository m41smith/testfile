
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

#reverser()
main()