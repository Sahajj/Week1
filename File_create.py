import os

# create a new file and write some text to it
filename = 'examp.txt'
with open(filename, 'w') as file:
    file.write('Hello, world!')

# rename the file
new_filename = 'new_example.txt'
os.rename(filename, new_filename)

# check that the file was renamed
if os.path.exists(new_filename):
    print(f'{filename} was renamed to {new_filename}')
else:
    print(f'Error: failed to rename {filename}')
