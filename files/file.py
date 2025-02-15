with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

print('\n------------Read File with new line-----------------\n')
# Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        # print(line) # add new line character at last of each line
        print(line.strip()) # remove the new line character

print('\n-------------Over write with new content----------------\n')
# This is over write the existing file content with new content
with open('example.txt', 'w') as file:
    file.write('Thank you everyone')
    file.write('Hope you are well\n')
    file.write('we will meet again.')

print('\n------------Read new content-----------------\n')
with open('example.txt', 'r') as file:
    content = file.read()
    print('New content ',content)

print('\n-----------Append data to file------------------\n')

with open('example.txt', 'a') as file:
    file.write('\n Appended data\n') # add only one line
    file.writelines(['Line 1\n','Line 2\n','Line 3\n'])


print('\n------------Read new content after append-----------------\n')
with open('example.txt', 'r') as file:
    content = file.read()
    print('New content ',content)