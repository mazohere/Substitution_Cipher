from itertools import cycle
import string

# assigning stuff for later
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
end = []



# reads the read file and prints its contents in the terminal
first = open('read.txt')
print(first.read)
original = first.read()

def final(end):

# writes the converted text into the write file and removes any existing text from the file
    converted = open('write.txt', 'w')
    for i in end:
        converted.write(i)

# convters the text into users choice
def converter(sub_num, orig, lower, upper):
    

    for i in orig:
        if i.islower():
            end.append(lower[int(lower.index(i) + int(sub_num)) % 26]) 
            print(lower[int(lower.index(i) + int(sub_num)) % 26])
        elif i.isupper():
            end.append(upper[int(upper.index(i) + int(sub_num)) % 26]) 
            print(upper[int(upper.index(i) + int(sub_num)) % 26])
        else:
            end.append(i)
            print(i)

    final(end)


def user_input():
    print('how many letters away would you like the cipher to be: ')
    choice = input(' ')

    if choice.isdigit() == True:
        print(type(choice))
        converter(choice, original, lowercase, uppercase)
    elif choice.isdigit() == False:
        print(type(choice))
        print('incorrect input, please try again')
        user_input()

user_input()

