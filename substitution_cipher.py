# reads the read file and prints its contents in the terminal
first = open('read.txt')
print(first.read)
original = first.read()

# convters the text into users choice
def converter(sub_num):
    # use the lambda thning
    print('i dont want any errors so im printing this')

def user_input():
    print('how many letters away would you like the cipher to be: ')
    choice = input(' ')

    if isinstance(choice, int) == True:
        converter()
    elif isinstance(choice, int) == False:
        print('incorrect input, please try again')
        user_input(choice)


# writes the converted text into the write file and removes any existing text from the file
converted = open('write.txt', 'w')
converted.write(original)