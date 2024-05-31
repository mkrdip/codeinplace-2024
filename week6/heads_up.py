import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'


def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines


def main():
    # m1: print all items on the list
    lines_list = get_words_from_file()
    # Find the data type of a variable
    # print(type(lines_list))
    # m2: show a randomly chosen word
    # print(random.choice(lines_list))
    # m3: continue when the user hits enter with another random word
    while True:
        random_word = random.choice(lines_list)
        print(random_word)
        # take enter as a blank input from the user
        input("Press enter to continue")
        

if __name__ == '__main__':
    main()
    
