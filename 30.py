# Open the first file for reading
with open('file1.txt', 'r') as file1:
    # Open the second file for reading
    with open('file2.txt', 'r') as file2:
        # Open a third file for writing
        with open('output.txt', 'w') as output:
            # Read the lines from both files simultaneously
            for line1, line2 in zip(file1, file2):
                # Remove any newline characters from the end of the lines
                line1 = line1.rstrip('\n')
                line2 = line2.rstrip('\n')
                # Combine the lines and write them to the output file
                output.write(f"{line1} {line2}\n")
