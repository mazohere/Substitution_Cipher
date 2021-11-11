# reads the read file and prints its contents in the terminal
first = open('read.txt')
print(first.read)
original = first.read()

# convters the text into users choice

# writes the converted text into the write file and removes any existing text from the file

converted = open('write.txt', 'w')
converted.write(original)