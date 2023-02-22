with open(C:\Users\panit\OneDrive - University of Central Missouri\Desktop\destination.txt, 'w') as f:
    # Write the keys on the first line
    keys_line = ','.join(data.keys()) + '\n'
    f.write(keys_line)
    # Write the values on the second line
    values_line = ','.join(data.values()) + '\n'
    f.write(values_line)