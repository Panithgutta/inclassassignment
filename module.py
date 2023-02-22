import configparser
from file_reader import read_file

# Read source and destination file names from config file
config = configparser.ConfigParser()
config.read('config.ini')

path = config['FILES']['path']
path2 = config['FILES']['path2']

# Read content from source file
source_content = read_file(path)

# Parse source content into a dictionary
source_dict = {}
for line in source_content.splitlines():
    key, value = line.split(': ')
    source_dict[key] = value

# Write keys and values to destination file
with open(path2, 'w') as f:
    f.write('\n'.join(source_dict.keys()) + '\n')
    f.write('\n'.join(str(v) for v in source_dict.values()) + '\n')
