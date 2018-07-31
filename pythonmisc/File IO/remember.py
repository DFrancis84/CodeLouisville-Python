import sys

def rememberer(thing):
    # open file and create a file
    with open("database.txt", "a") as file:
        # write thing to file
        file.write(thing+"\n")


def show():
    # open file
    with open("database.txt") as file:
        for line in file:
            print(line)

    
# if __name__== '__main__':
#   rememberer(input("What should I remember? "))

if __name__== '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememberer(' '.join(sys.argv[1:]))